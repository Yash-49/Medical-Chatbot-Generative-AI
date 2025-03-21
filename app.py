from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
import logging

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

# ✅ Load environment variables
load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# ✅ Validation
if not PINECONE_API_KEY or not GOOGLE_API_KEY:
    raise ValueError("Missing PINECONE or GOOGLE API Key!")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# ✅ Debug: Print API keys (hide in production)
logging.debug(f"PINECONE_API_KEY: {PINECONE_API_KEY[:5]}...")  # Hide full key for security
logging.debug(f"GOOGLE_API_KEY: {GOOGLE_API_KEY[:5]}...")

# ✅ Initialize embeddings
try:
    embeddings = download_hugging_face_embeddings()
    logging.info("✅ HuggingFace embeddings loaded successfully.")
except Exception as e:
    logging.error(f"❌ Error loading embeddings: {e}")
    raise e

# ✅ Connect to Pinecone
try:
    index_name = "medicalbot"
    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )
    logging.info("✅ Connected to Pinecone index.")
except Exception as e:
    logging.error(f"❌ Error connecting to Pinecone: {e}")
    raise e

# ✅ Configure retriever
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# ✅ Gemini LLM Initialization
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro-latest",
        temperature=0,
        google_api_key=GOOGLE_API_KEY,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
    logging.info("✅ Gemini LLM initialized successfully.")
except Exception as e:
    logging.error(f"❌ Error initializing Gemini LLM: {e}")
    raise e

# ✅ Create RAG chain
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# ✅ Routes
@app.route("/")
def home():
    return render_template('chat.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route("/get", methods=["GET", "POST"])
def chat():
    try:
        msg = request.form["msg"]
        logging.info(f"User Input: {msg}")

        response = rag_chain.invoke({"input": msg})
        logging.info(f"RAG Response: {response}")

        return str(response["answer"])

    except Exception as e:
        logging.error(f"❌ Error during chat generation: {e}")
        return "An error occurred. Please try again."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
