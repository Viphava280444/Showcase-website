import smtplib, ssl
import os
from dotenv import load_dotenv
load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 587

    username = os.getenv('EMAIL2')
    password = os.getenv('API_EMAIL_KEY')

    receivers = [os.getenv('EMAIL1'), os.getenv('EMAIL2')]
    context = ssl.create_default_context()

    # messages = """\
    # Subject: Check Port 587
    # Hi, How are you

    # """

    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.login(username, password)
        for index, email in enumerate(receivers):
            server.sendmail(username, email, message)