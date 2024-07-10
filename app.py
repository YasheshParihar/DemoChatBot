import streamlit as st

# st.title("hey")

# --- PAGE SETUP ---
# about_company = st.Page(
#     "views/about_company.py",
#     title="About Company",
#     icon=":material/account_circle:",
#     default=True,
# )
project_1_page = st.Page(
    "views/flow_diagram.py",
    title="Flow diagram",
    icon=":material/account_circle:",
    default=True,
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)


# # --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_company, project_1_page, project_2_page])

# # --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        
        "Create Your ChatBot": [project_1_page, project_2_page],
    }
)
# --- RUN NAVIGATION ---
pg.run()