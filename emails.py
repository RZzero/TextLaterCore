#!/usr/bin/python


#For now we're limited to send emails without attachments.
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from message import Message

                    #  message refers to a message object
def send_email_gmail(user_mail, user_pass, message):
    msg = MIMEMultipart()
    msg['From'] = message.sender
    to_str = ", ".join(message.to_m) #Preparing string of emails
    msg['To'] = to_str
    msg['Subject'] = message.subject
    msg_body = message.content
    msg.attach(MIMEText(msg_body, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com:465')
        server.login(user_mail, user_pass)

        msg_to_be_send = msg.as_string()

        server.sendmail(message.sender, message.to_m, msg_to_be_send)
        server.quit()
    except Exception:
        print("Unable to send message")
