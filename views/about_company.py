import streamlit as st

st.title("About Company")
from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()


# # --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:  
    st.image("./assets/profilepic.png", width=230)

with col2:
    st.title("Yashesh Singh Parihar", anchor=False)
    st.write(
        "Skilss : NLP, ML, DL, AWS "
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# # --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("About Us", anchor=False)
st.write(
    """
    - Axe Digital is a growth marketing fuelled by technology and driven by a talented team of consultative marketers, creatives, analysts and technologists. We ignite revenue growth and brand recognition for leading and emerging around the world.Marketing is no longer about a singular offer or what your brand presents visually. 
    - Is a sprawling journey with countless touchpoints.
    - Consumer shops with their values and gravitate towards brands they trust. They want to be a part of a tribe. A story. Whats more, the path to purchase needs to be fast, frictionless and personable.
    - Marketing should be a strategic business driver, a road that leads to profitable revenue growth and brand lift.
    - We take the guesswork out of marketing, making the most from your investment so you get what you care about growth, handled from planning to execution.
    - Our experienced team develops custom marketing playbooks fueled by data, market trends and industry insights to set you apart from the competition, designed to drive revenue and brand lift.
    - Thats why we are in the business of igniting growth and brand recognition for the brands we are lucky to call our clients.
    - Get in Touch Now!

    """
)

# # --- SKILLS ---
st.write("\n")
st.subheader("For Help ", anchor=False)
st.write(
    """
        - Mail Id : yasheshsingh@arthat.org
        - Phone no. : 91+ 9687169696
    """
)