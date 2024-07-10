import streamlit as st
from PIL import Image
import re
import PyPDF2
import phonenumbers
from phonenumbers import geocoder, carrier

# For taking valid mail id
def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

# Function to parse and validate phone number
def parse_phone_number(number, region):
    try:
        parsed_number = phonenumbers.parse(number, region)
        if phonenumbers.is_valid_number(parsed_number):
            return parsed_number
        else:
            st.error("Invalid phone number")
            return None
    except phonenumbers.NumberParseException as e:
        st.error(f"NumberParseException: {str(e)}")
        return None
    
# User name inputs
company_name = st.text_input('Company Name')

# Image Uploader
st.text("Upload Company's Logo")
image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

email = st.text_input('Email ID')

# Phone number input
phone_number = st.text_input("Enter phone number:")
region_code = st.text_input("Enter region code (e.g., US, IN):")
# Parse and validate phone number
if phone_number and region_code:
    parsed_number = parse_phone_number(phone_number, region_code)
    
    if parsed_number:
        # Display formatted phone number
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        st.write("Formatted phone number:", formatted_number)

        # Display region information
        region = geocoder.description_for_number(parsed_number, "en")
        st.write("Region:", region)

        # Display carrier information
        carrier_name = carrier.name_for_number(parsed_number, "en")
        st.write("Carrier:", carrier_name)

# Business category dropdown
business_category = st.selectbox("Business Category", ["Technology", "Healthcare", "Finance", "Education", "Marketing" ,"Others"])

# Additional information dropdown and inputs
additional_info_type = st.selectbox("Additional Information", ["Custom Text", "Website URL", "File Upload"])
additional_info_value = None
if additional_info_type == "Custom Text":
    additional_info_value = st.text_area("Enter your custom text")
elif additional_info_type == "Website URL":
    additional_info_value = st.text_input("Enter the website URL")
elif additional_info_type == "File Upload":
    additional_info_value = st.file_uploader("Choose a file", type=["txt", "pdf", "docx", "xlsx"])

# Submit button
st.markdown(
    """
    <style>
    .submit-button {
        display: flex;
        justify-content: flex-end;
    }
    </style>
    """, unsafe_allow_html=True
)

submit_button = st.button("Submit")

if submit_button:
    if not company_name:
        st.error("Please provide your company name.", icon="🏢")
        st.stop()

    if not email:
        st.error("Please provide your email address.", icon="📨")
        st.stop()

    if not is_valid_email(email):
        st.error("Please provide a valid email address.", icon="📧")
        st.stop()

    if not phone_number:
        st.error("Please provide your phone number.", icon="📞")
        st.stop()

    if not region_code:
        st.error("Please provide your region code.", icon="🌍")
        st.stop()

    if not parsed_number:
        st.error("Please provide a valid phone number.", icon="❌")
        st.stop()

    if additional_info_type == "Custom Text" and not additional_info_value:
        st.error("Please provide custom text.", icon="✏️")
        st.stop()

    if additional_info_type == "Website URL" and not additional_info_value:
        st.error("Please provide a website URL.", icon="🌐")
        st.stop()

    if additional_info_type == "File Upload" and not additional_info_value:
        st.error("Please upload a file.", icon="📁")
        st.stop()

    st.success("Your form has been submitted successfully! 🎉", icon="🚀")
    

