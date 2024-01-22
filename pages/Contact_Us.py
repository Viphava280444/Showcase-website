import streamlit as st
from sent_email import send_email as se

st.header("Contact Me")

with st.form(key= 'email_forms'):
    user_email = st.text_input("Your email address")
    topic = st.selectbox('What topic do you want to discuss', ('Project', 'Machine-learning', 'Report', 'Other'))
    message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email} on topic about {topic}

From: {user_email}
Topic: {topic}
{message}


"""
    button = st.form_submit_button("Submit")
    if button:
        se(message)
        st.info('Your email was sent successfully')
        