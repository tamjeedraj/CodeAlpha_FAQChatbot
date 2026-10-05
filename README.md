# 🤖 CodeAlpha FAQ AI Chatbot

An AI-powered FAQ chatbot built as part of the **CodeAlpha Artificial Intelligence Internship**.

The chatbot uses **Natural Language Processing, semantic search, FAISS vector search, RAG, and Google's Gemini API** to understand user questions and generate relevant, natural-language answers from a custom FAQ knowledge base.

---

## 📌 Project Overview

Traditional FAQ systems usually depend on exact keyword matching. This project uses **semantic similarity** to understand the meaning behind a user's question.

The system:

1. Receives a user's question.
2. Preprocesses the question using NLP.
3. Converts the question into a vector embedding.
4. Searches the FAQ knowledge base using FAISS.
5. Retrieves the most relevant FAQs.
6. Sends the retrieved context to Gemini.
7. Generates a concise and grounded response.
8. Displays the answer through a Streamlit chat interface.

---

## ✨ Features

* 💬 Interactive chatbot interface
* 🧠 NLP-based text preprocessing
* 🔤 Semantic text embeddings
* 🔎 FAISS similarity search
* 📚 Custom FAQ knowledge base
* 🤖 AI Agent workflow
* ✨ Gemini API integration
* 📖 Retrieval-Augmented Generation (RAG)
* 🎯 Retrieval confidence score
* 🔎 View retrieved FAQ sources
* 🗑️ Clear chat functionality
* 🔐 Environment-based API key protection

---

## 🛠️ Technologies Used

| Technology            | Purpose                                   |
| --------------------- | ----------------------------------------- |
| Python                | Core programming language                 |
| Streamlit             | Web-based chatbot interface               |
| spaCy                 | NLP preprocessing                         |
| Sentence Transformers | Text embeddings                           |
| FAISS                 | Vector similarity search                  |
| Gemini API            | AI response generation                    |
| RAG                   | Grounded answer generation                |
| AI Agent              | Query processing and decision workflow    |
| JSON                  | FAQ knowledge base                        |
| uv                    | Python package and environment management |
| Git & GitHub          | Version control and source code hosting   |

---

## 🏗️ Project Architecture

```text
                 👤 User
                    │
                    ▼
            🎨 Streamlit UI
                    │
                    ▼
              🤖 AI Agent
                    │
                    ▼
          🧠 NLP Preprocessing
                 (spaCy)
                    │
                    ▼
       🔤 Sentence Transformer
              Embeddings
                    │
                    ▼
              🔎 FAISS
          Semantic Retrieval
                    │
                    ▼
             📚 FAQ Context
                    │
                    ▼
              ✨ Gemini API
                    │
                    ▼
             💬 Final Answer
```

---

## 📂 Project Structure

```text
CodeAlpha_FAQChatbot/
│
├── data/
│   └── faqs.json
│
├── app.py
├── agent.py
├── rag.py
├── embeddings.py
├── llm.py
├── preprocess.py
├── config.py
│
├── .env.example
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/tamjeedraj/CodeAlpha_FAQChatbot.git
```

### 2. Open the project

```bash
cd CodeAlpha_FAQChatbot
```

### 3. Install dependencies

This project uses `uv`.

```bash
uv sync
```

If you don't have `uv` installed, install it first according to the official uv documentation.

---

## 🔑 Gemini API Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**Never upload your `.env` file to GitHub.**

The `.gitignore` file is configured to prevent the API key from being committed.

---

## 🧠 spaCy Model

Install the required English spaCy model:

```bash
uv run python -m spacy download en_core_web_sm
```

You can verify the installation with:

```bash
uv run python -c "import spacy; nlp=spacy.load('en_core_web_sm'); print('spaCy model OK')"
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
uv run streamlit run app.py
```

The application will open in your browser.

---

## 💬 Example Questions

You can ask questions such as:

```text
What is NLP?
```

```text
What is machine learning?
```

```text
What is RAG?
```

```text
What is an AI agent?
```

```text
How can I improve this chatbot?
```

The chatbot searches the FAQ knowledge base and generates a relevant response.

---

## 📚 FAQ Knowledge Base

The chatbot uses a custom JSON knowledge base:

```text
data/faqs.json
```

New questions and answers can easily be added to this file.

Example:

```json
{
  "id": 21,
  "question": "What is deep learning?",
  "answer": "Deep learning is a subset of machine learning that uses neural networks with multiple layers to learn complex patterns."
}
```

---

## 🔎 How RAG Works in This Project

The project follows a simple Retrieval-Augmented Generation pipeline:

```text
User Question
      ↓
Text Preprocessing
      ↓
Generate Embedding
      ↓
FAISS Similarity Search
      ↓
Retrieve Relevant FAQs
      ↓
Build Context
      ↓
Send Context to Gemini
      ↓
Generate Answer
```

This approach helps the chatbot provide answers based on the project's FAQ knowledge base instead of relying entirely on the language model's general knowledge.

---

## 🛡️ Handling Unknown Questions

If a question does not have a sufficiently relevant FAQ match, the chatbot can return a fallback response instead of generating unsupported information.

This helps reduce hallucinated answers and keeps the chatbot focused on its knowledge base.

---

## 🎯 Internship Task

This project was developed for:

**CodeAlpha Artificial Intelligence Internship — Task 2: Chatbot for FAQs**

The implementation covers the major requirements:

* ✅ FAQ collection
* ✅ NLP preprocessing
* ✅ Similarity-based matching
* ✅ Semantic search
* ✅ AI-generated responses
* ✅ Interactive chatbot interface

---

## 🚀 Future Improvements

Possible improvements include:

* Conversation memory
* Better document ingestion
* Hybrid keyword + semantic search
* Reranking models
* Streaming Gemini responses
* Admin panel for managing FAQs
* User authentication
* Analytics dashboard
* Automated FAQ evaluation
* Multi-language support
* Voice input and text-to-speech

---

## 🔐 Security

The Gemini API key is stored using an environment variable.

```text
.env
```

The `.env` file should **never be committed or pushed to GitHub**.

---

## 👨‍💻 Author

**Tamjeed Raj**

GitHub:

https://github.com/tamjeedraj/CodeAlpha_FAQChatbot

---

## 📄 License

This project was created for educational and internship purposes.
