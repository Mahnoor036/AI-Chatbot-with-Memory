import os
import streamlit as st
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import CharacterTextSplitter

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 AI Chatbot with Memory")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Upload PDF
pdf = st.file_uploader("Upload a PDF file", type="pdf")

if pdf:
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())

    loader = PyPDFLoader("temp.pdf")
    pages = loader.load()

    # Split PDF into chunks
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(pages)

    # Create embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectordb = Chroma.from_documents(docs, embedding=embeddings)

    # Memory buffer
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # QA chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(temperature=0, openai_api_key=openai_api_key),
        retriever=vectordb.as_retriever(),
        memory=memory
    )

    # User input
    user_input = st.text_input("Ask a question about your PDF:")

    if user_input:
        answer = qa_chain.run(user_input)
        st.session_state.chat_history.append(("User", user_input))
        st.session_state.chat_history.append(("Bot", answer))

    # Display chat history
    for speaker, msg in st.session_state.chat_history:
        st.markdown(f"**{speaker}:** {msg}")
