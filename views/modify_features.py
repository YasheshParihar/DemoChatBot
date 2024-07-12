import streamlit as st

def show():
    st.title("Modify ChatBot Features")

    model_choices = ["gpt-3.5-turbo", "gpt-4", "gemini-1.0-pro"]
    st.selectbox("Select Model", model_choices, key="model_name")
    st.slider("Temperature", 0.0, 1.0, 0.7, key="temperature")
    st.number_input("Max Tokens", 50, 2048, 200, key="max_tokens")

    if st.button("Save Changes"):
        save_chatbot_settings()
        st.success("Changes saved successfully!")

def save_chatbot_settings():
    # Implement this function to save chatbot settings to your database
    pass