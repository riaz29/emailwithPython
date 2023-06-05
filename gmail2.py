from email.message import EmailMessage
import ssl
import smtplib

user_email = "your@gmail.com"
user_password = "app_password"
receipent_email = "receiver@gmail.com"
email_subject = "Subject of Your Email"
email_body = """
    Define Body Part Here
"""
emailObj = EmailMessage()
emailObj['From'] = user_email
emailObj['To'] = receipent_email
emailObj['Subject'] = email_subject
emailObj.set_content(email_body) 

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
    smtp.login(user_email,user_password)
    smtp.sendmail(user_email,receipent_email,emailObj.as_string())
