import streamlit as st
import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import PyPDF2
import io

def show():
    st.title("Data Upload")

    if 'vector_store' not in st.session_state:
        st.session_state.vector_store = None

    if 'chatbot_name' not in st.session_state:
        st.session_state.chatbot_name = ""

    chatbot_name = st.text_input("Chatbot Name", key="chatbot_name_input", value=st.session_state.chatbot_name)

    # File upload
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    pdf_text = ""
    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)

    # Website URL input
    website_url = st.text_input("Enter website URL")
    website_content = ""
    if website_url:
        website_content = fetch_website_content(website_url)

    # Custom text input
    custom_text = st.text_area("Enter custom text (optional)")

    if st.button("Create/Update Chatbot"):
        if not chatbot_name:
            st.error("Please enter a chatbot name.")
        elif not pdf_text and not website_content and not custom_text:
            st.error("Please provide at least one source of data (PDF, website, or custom text).")
        else:
            combined_text = pdf_text + " " + website_content + " " + custom_text
            create_or_update_chatbot(chatbot_name, combined_text)
            st.session_state.chatbot_name = chatbot_name
            st.success(f"Chatbot '{chatbot_name}' has been created/updated successfully!")

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def fetch_website_content(url, max_pages=5):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except Exception as e:
        st.error(f"Error fetching website content: {str(e)}")
        return ""

def create_or_update_chatbot(name, text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings()
    
    if st.session_state.vector_store is None:
        st.session_state.vector_store = FAISS.from_texts(texts, embeddings)
    else:
        st.session_state.vector_store.add_texts(texts)

    # We're not setting st.session_state.chatbot_name here anymore