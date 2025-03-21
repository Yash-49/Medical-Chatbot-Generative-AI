
# 🩺 **Medical-Chatbot-Generative-AI**

![Medical Chatbot](https://img.shields.io/badge/Generative%20AI-Chatbot-brightgreen) ![Tech Stack](https://img.shields.io/badge/Tech%20Stack-Python%20%7C%20Flask%20%7C%20Pinecone%20%7C%20Gemini%20AI-blue) ![Version](https://img.shields.io/badge/Version-1.0-yellow)

### 💡 **Overview**
The **Medical Chatbot with Generative AI** is an advanced AI-powered assistant designed to provide **accurate and instant responses** to medical queries. It utilizes **Hugging Face embeddings**, **Google Gemini AI**, and **Pinecone** as a vector store to efficiently **retrieve and generate accurate responses**. The chatbot also includes **voice input** and **text-to-speech (TTS)** output for an interactive experience.

---

## ✅ **Features**
- 🔍 **Natural Language Processing (NLP)**: Understands and processes medical queries in natural language.  
- ⚡ **Vector-based Retrieval**: Uses **Pinecone** for efficient retrieval of relevant medical information.  
- 🗨️ **Generative AI Responses**: Uses **Google Gemini AI** for contextually accurate and informative responses.  
- 🎤 **Voice Input & TTS Output**:  
    - Users can **speak their queries** using voice input.  
    - The bot can **speak the response** aloud using **Text-to-Speech (TTS)**.  
- 🎯 **Responsive UI**:  
    - Modern, user-friendly chat interface with **Bootstrap styling**.  
    - TTS listen button with hover functionality.  
- 🚀 **Error Handling & Logging**:  
    - Displays error messages for invalid inputs.  
    - Robust logging for easy debugging.  

---

## 🛠️ **Tech Stack**
| **Component**         | **Technology Used**                |
|------------------------|----------------------------------|
| **Backend Framework**  | Flask                             |
| **LLM**                | Google Gemini AI (1.5 Pro Latest) |
| **Vector Database**    | Pinecone                          |
| **Embeddings**         | Hugging Face (all-MiniLM-L6-v2)   |
| **Frontend**           | HTML, CSS, Bootstrap              |
| **TTS & Voice Input**  | JavaScript Web Speech API         |
| **Environment Config** | dotenv for API key management     |

---

## 🔥 **Project Architecture**

```
📂 Medical-Chatbot-Generative-AI
 ┣ 📂 src
 ┃ ┣ 📜 helper.py         → PDF loading, embedding, and text splitting
 ┃ ┣ 📜 prompt.py         → Prompt configuration for Gemini AI
 ┣ 📂 static
 ┃ ┣ 📜 style.css         → Frontend styling
 ┣ 📂 templates
 ┃ ┣ 📜 chat.html         → Chat interface HTML file
 ┣ 📜 app.py              → Flask application entry point
 ┣ 📜 requirements.txt    → Python dependencies
 ┣ 📜 .env                → API keys configuration
 ┣ 📜 README.md           → Project documentation
```

---

## 🚀 **Getting Started**

### ✅ **1. Clone the Repository**
```bash
git clone https://github.com/your-username/Medical-Chatbot-Generative-AI.git
cd Medical-Chatbot-Generative-AI
```

### ✅ **2. Create a Virtual Environment**
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### ✅ **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### ✅ **4. Set Up Environment Variables**
Create a `.env` file in the root directory and add the following:
```plaintext
PINECONE_API_KEY=YOUR_PINECONE_API_KEY
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

### ✅ **5. Run the Application**
```bash
python app.py
```
- The chatbot will be accessible at:  
📌 `http://127.0.0.1:8080`

---

## ⚙️ **Configuration Details**

### 🔹 **Pinecone Vector Store**
- The project uses **Pinecone** to **store and retrieve embeddings**.
- Ensure you have created an index named `medicalbot` in your Pinecone console.

### 🔹 **Gemini AI**
- The chatbot uses **Google Gemini AI (1.5 Pro Latest)** for generating responses.  
- Make sure you have the **Gemini API key** added in the `.env` file.

---

## 💻 **Usage**

### ✅ **1. Medical Query Interaction**
- You can **type your medical queries** or **use voice input**.
- The bot will provide **relevant, accurate answers** by:  
    - Retrieving medical information from the Pinecone vector database.  
    - Generating an AI-based response using **Google Gemini AI**.

### ✅ **2. Text-to-Speech Output**
- **Click the "Listen" button** to hear the bot's response.  
- The bot uses **natural TTS voices** with customizable pitch and rate.

---

## 📦 **API Endpoints**

| **Method**   | **Endpoint**   | **Description**               |
|--------------|----------------|--------------------------------|
| `GET /`      | `/`            | Renders the chatbot interface  |
| `POST /get`  | `/get`         | Handles user queries           |

---

## 🛠️ **Customization**

### 🔥 **1. Change the Embedding Model**
To use a different **Hugging Face embedding model**, modify this line in `helper.py`:
```python
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
```
✅ You can replace `'all-MiniLM-L6-v2'` with other models like:
- `sentence-transformers/all-mpnet-base-v2`  
- `sentence-transformers/paraphrase-MiniLM-L12-v2`  

---

### 🔥 **2. Adjust TTS Settings**
To change the **speech rate, pitch, or volume**, modify the `speakText()` function in `chat.html`:
```javascript
utterance.rate = 1.0;      // Speed
utterance.pitch = 1.0;     // Pitch
utterance.volume = 1.0;    // Volume
```

---

## 🛠️ **Troubleshooting**

### ❗ **Common Issues**
- **TTS Not Working:**  
    - Check the browser console logs.  
    - Ensure you have `window.speechSynthesis` enabled.  
- **API Key Errors:**  
    - Verify the `.env` file contains the correct Pinecone and Gemini API keys.  
- **No Embeddings Found:**  
    - Ensure your Pinecone index name matches the one in the code (`medicalbot`).  
- **Voice Not Detected:**  
    - Ensure microphone permissions are enabled in your browser.

---

## 📚 **References**
- [Flask](https://flask.palletsprojects.com/)
- [Pinecone](https://www.pinecone.io/)
- [Google Gemini AI](https://ai.google.dev/)
- [Hugging Face Embeddings](https://huggingface.co/)

---

## 📜 **License**
This project is licensed under the **MIT License**.  
Feel free to use, modify, and share! 🚀

---

## 🙌 **Contributors**
- 👤 **Yash Patel**  
  📧 [Email](mailto:your-email@example.com)  
  💼 [LinkedIn](https://www.linkedin.com/in/your-profile)
