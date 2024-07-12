import streamlit as st
from views import about, company_info, chatbot, modify_features, data_upload

st.set_page_config(page_title="Arthat ChatBot", layout="wide")

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'about'

# Custom CSS
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
    }
    .stSelectbox>div>div>select {
        background-color: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    if st.button("About Arthat ChatBot"):
        st.session_state.current_page = 'about'
    if st.button("Company Information"):
        st.session_state.current_page = 'company_info'
    if st.button("Data Upload"):
        st.session_state.current_page = 'data_upload'
    if st.button("Chat Bot"):
        st.session_state.current_page = 'chatbot'
    if st.button("Modify Features"):
        st.session_state.current_page = 'modify_features'

# Display the selected page
if st.session_state.current_page == 'about':
    about.show()
elif st.session_state.current_page == 'company_info':
    company_info.show()
elif st.session_state.current_page == 'data_upload':
    data_upload.show()
elif st.session_state.current_page == 'chatbot':
    chatbot.show()
elif st.session_state.current_page == 'modify_features':
    modify_features.show()