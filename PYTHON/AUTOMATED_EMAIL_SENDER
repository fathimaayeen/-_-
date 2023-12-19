import os
import smtplib
from email.message import EmailMessage
import ssl

# Replace these placeholders with your email credentials
sender_email = "sender_email"
sender_password = "Password"
to_email = "receiver_email"    
subject = "Scheduled Reminder"
body = "This email is send using Python"  
em=EmailMessage()
em['From']=sender_email
em['To']=to_email
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(sender_email,sender_password)
    smtp.sendmail(sender_email,to_email,em.as_string())








