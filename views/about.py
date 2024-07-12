import streamlit as st

def show():
    st.title("Welcome to Arthat ChatBot")
    
    st.markdown("""
    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px;">
    <h2>Your AI-Powered Business Assistant</h2>
    Arthat ChatBot is your intelligent solution for creating custom chatbots tailored to your business needs. 
    Follow these simple steps to get started:

    1. **Company Information**: Provide details about your company.
    2. **Upload Data**: Add your business content through PDF files, website URLs, or custom text.
    3. **Customization**: Tailor your chatbot to your specific requirements.
    4. **Deployment**: Launch your chatbot and start engaging with customers.

    Experience the power of AI in enhancing your customer interactions!
    </div>
    """, unsafe_allow_html=True)

    if st.button("Create New ChatBot"):
        st.session_state.current_page = 'company_info'
    
    st.header("Load Existing ChatBot")
    available_chatbots = load_existing_chatbots()
    if available_chatbots:
        selected_chatbot = st.selectbox("Select a chatbot", available_chatbots)
        if selected_chatbot and st.button("Load ChatBot"):
            load_chatbot(selected_chatbot)
            st.session_state.current_page = 'chatbot'
    else:
        st.info("No existing chatbots found.")

def load_existing_chatbots():
    # Implement this function to load existing chatbot names from your database
    return []

def load_chatbot(chatbot_name):
    # Implement this function to load the selected chatbot's data
    pass