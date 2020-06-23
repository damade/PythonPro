import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'your name'
email['to'] = 'recipient email'
email['subject'] = 'I am trying to practice sending email through Python'

email.set_content("I am becoming a full stack Python developer")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('youremail', 'password')  # Ensure you've override your security settings to accept third party
    smtp.send_message(email)  # to login to your account and perform operations.
    print("We are done and we are good")
