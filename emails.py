#!/usr/bin/python
#For now we're limited to send emails without attachments.
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from message import Message


def send_email_gmail(user_mail, user_pass, to_, subject_, content_):
    msg = MIMEMultipart()
    msg['From'] = user_mail
    to_str = ", ".join(to_) #Preparing string of emails
    msg['To'] = to_str
    msg['Subject'] = subject_
    msg_body = content_
    msg.attach(MIMEText(msg_body, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com:465')
        server.login(user_mail, user_pass)

        msg_to_be_send = msg.as_string()

        server.sendmail(user_mail, to_, msg_to_be_send)
        server.quit()
    except Exception:
        print("Unable to send message")

if __name__ == "__main__":
    emails = [""]
    send_email("", "", emails, "", "")
