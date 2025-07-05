# 🧠 AI Chatbot with Memory (LangChain + OpenAI + Streamlit)

An intelligent chatbot app that remembers previous interactions and can answer questions from long documents (like PDFs). Built using **LangChain**, **OpenAI**, **ChromaDB**, and **Streamlit**.

---

## 📌 Features

- ✅ Chat interface using **Streamlit**
- 📚 Upload a **PDF file** and ask questions about its contents
- 🧠 Uses **LangChain's ConversationalRetrievalChain** for memory-based QA
- 🔎 Embedding and semantic search via **ChromaDB**
- 🔐 Secure API key management with `.env`

---

## 🚀 Live Demo

> Coming soon (you can deploy this easily on [Streamlit Cloud](https://streamlit.io/cloud))!

---


## 🛠️ Tech Stack

| Tool      | Purpose                     |
|-----------|-----------------------------|
| [LangChain](https://python.langchain.com/) | Conversational logic & memory  |
| [OpenAI API](https://platform.openai.com/) | GPT language model              |
| [Streamlit](https://streamlit.io/)     | Web UI for the chatbot         |
| [ChromaDB](https://www.trychroma.com/) | Vector storage for PDF content |
| [dotenv](https://pypi.org/project/python-dotenv/) | Load API keys from `.env` file  |

---

## 📂 Project Structure

```bash
model/
├── chatbot_app.py       # Main Streamlit app
├── .env                 # Your OpenAI secret key (NOT tracked in Git)
├── .env.example         # Sample env file (for GitHub)
├── .gitignore
└── requirements.txt     # Python dependencies
