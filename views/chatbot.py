import streamlit as st
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

# Ensure you set your OpenAI API key securely
os.environ["OPENAI_API_KEY"] = st.secrets["openai_api_key"]

def show():
    st.title("Your Custom ChatBot")

    if 'vector_store' not in st.session_state or st.session_state.vector_store is None:
        st.warning("Please create a chatbot first by uploading data.")
        return

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.subheader("Chat History")
    chat_container = st.container()
    
    with chat_container:
        for i, (question, answer) in enumerate(st.session_state.chat_history):
            st.text_area(f"Q{i+1}", value=question, height=50, disabled=True)
            st.text_area(f"A{i+1}", value=answer, height=100, disabled=True)

    question = st.text_input("Ask a question:", key="user_question")
    if question:
        with st.spinner("Generating answer..."):
            answer = answer_question(st.session_state.vector_store, question)
        st.session_state.chat_history.append((question, answer))
        st.experimental_rerun()

def answer_question(vector_store, question):
    llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vector_store.as_retriever())
    return qa_chain.run(question)