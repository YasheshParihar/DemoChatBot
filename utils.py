import os
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            return "\n".join([para.get_text() for para in paragraphs])
        else:
            return "Failed to retrieve the website content."
    except Exception as e:
        return str(e)

def create_chroma_db(text, path, name):
    chunks = split_text(text)
    chroma_client = chromadb.PersistentClient(path=path)
    db = chroma_client.create_collection(name=name)
    for i, chunk in enumerate(chunks):
        db.add(documents=[chunk], ids=[str(i)])
    return db, name

def load_chroma_collection(path, name):
    chroma_client = chromadb.PersistentClient(path=path)
    return chroma_client.get_collection(name=name)

def split_text(text, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)

def get_relevant_passage(query, db, n_results=1):
    results = db.query(query_texts=[query], n_results=n_results)
    return results['documents'][0] if results['documents'] else []

def make_rag_prompt(query, relevant_passage):
    return f"""Answer the following question based on the given context:
Question: {query}
Context: {relevant_passage}
Answer:"""

def generate_answer(prompt, model_name, temperature, max_tokens):
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "system", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content