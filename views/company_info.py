import streamlit as st
import re
import phonenumbers

def show():
    st.title("Company Information")

    col1, col2 = st.columns(2)

    with col1:
        company_name = st.text_input('Company Name', key="company_name")
        email = st.text_input('Email ID', key="email")
        phone_number = st.text_input("Phone Number", key="phone_number")
        region_code = st.text_input("Region Code (e.g., US, IN)", key="region_code")

    with col2:
        st.text("Upload Company's Logo")
        image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="logo")
        business_category = st.selectbox("Business Category", 
                                         ["Technology", "Healthcare", "Finance", "Education", "Marketing", "Others"],
                                         key="business_category")

    if st.button("Next: Upload Data"):
        if validate_inputs(company_name, email, phone_number, region_code):
            save_company_info()
            st.session_state.current_page = 'data_upload'

def validate_inputs(company_name, email, phone_number, region_code):
    if not company_name:
        st.error("Please provide your company name.")
        return False
    if not email or not is_valid_email(email):
        st.error("Please provide a valid email address.")
        return False
    if not phone_number or not region_code or not is_valid_phone(phone_number, region_code):
        st.error("Please provide a valid phone number and region code.")
        return False
    return True

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def is_valid_phone(number, region):
    try:
        parsed_number = phonenumbers.parse(number, region)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False

def save_company_info():
    # Implement this function to save company info to your database
    pass