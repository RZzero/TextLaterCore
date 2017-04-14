#!/usr/bin/python


#For now we're limited to send emails without attachments.
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename
from message import Message

                    #  message refers to a message object
def send_email_gmail(user_mail, user_pass, message, files):
    msg = MIMEMultipart()
    msg['From'] = message.sender
    to_str = ", ".join(message.to_m) #Preparing string of emails
    msg['To'] = to_str
    msg['Subject'] = message.subject
    msg_body = message.content
    msg.attach(MIMEText(msg_body, 'plain'))

    if len(files) > 0:
        for f in files:
            with open(f, "r") as fil:
                part = MIMEApplication(
                    fil.read(),
                )
                part['Content-Disposition'] = 'attachment; filename="{0}"'.format(basename(f))
                msg.attach(part)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com:465')
        server.login(user_mail, user_pass)

        msg_to_be_send = msg.as_string()

        server.sendmail(message.sender, message.to_m, msg_to_be_send)
        server.quit()
    except Exception:
        print("Unable to send message")
