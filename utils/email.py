import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pydantic import EmailStr
from dotenv import load_dotenv

# Load environment variables from .env.dev
load_dotenv(dotenv_path='.env')

def send_assessment_email(student_email: EmailStr, assessment_link: str):
    # Email configuration from environment variables
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    # Create the email content
    message = MIMEMultipart("alternative")
    message["Subject"] = "Your Assessment Link"
    message["From"] = sender_email
    message["To"] = student_email

    text_content = f"Hello,\n\nPlease complete your assessment using the following link:\n{assessment_link}\n\nBest regards,\nAssessment Team"
    html_content = f"""
    <html>
        <body>
            <p>Hello,</p>
            <p>Please complete your assessment using the following link:</p>
            <a href="{assessment_link}">Start Assessment</a>
            <p>Best regards,<br>Assessment Team</p>
        </body>
    </html>
    """

    # Attach the email content to the message
    message.attach(MIMEText(text_content, "plain"))
    message.attach(MIMEText(html_content, "html"))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade to a secure connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, student_email, message.as_string())
        server.quit()
        print(f"Assessment link sent to {student_email}")
    except smtplib.SMTPException as smtp_error:
        print(f"SMTP error occurred: {smtp_error}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
