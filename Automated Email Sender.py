# email_sender.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

def send_email(subject, message, to_email):
    """
    Send an email.

    Args:
    - subject (str): Email subject.
    - message (str): Email body.
    - to_email (str): Recipient's email address.
    """
    # Your email credentials
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'

    # Setup the MIME
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = to_email
    email_message['Subject'] = subject

    # Attach the message to the email
    email_message.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(email_message)

def job():
    """
    Job to be scheduled for sending automated emails.
    """
    subject = "Automated Email"
    message = "This is a scheduled automated email. You can customize the content here."
    to_email = "recipient@example.com"
    
    send_email(subject, message, to_email)
    print("Email sent!")

# Schedule the job to run every day at a specific time (e.g., 10:00 AM)
schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
