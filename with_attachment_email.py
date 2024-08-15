import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import date
from datetime import datetime

# Set up port
smtp_port = 587  # Stanndard secure SMTP port
smtp_server = "smtp.gmail.com"  # google smtp server
email_from = "bikashchamua555@gmail.com"
email_list = ["bikashchamua555@gmail.com", "bikashchamua537@gmail.com"]
password = "eaguhgnopcgruokc"
subject = "New email from bikash with attachment "


def send_emails(email_list):
    for person in email_list:
        # Make the body of the email
        now = datetime.now()
        body = f"""
Hello Teacher,
    Here is the attendance for today's {date.today()} class 
    recorded at {now.strftime("%H:%M:%S")}.
    CSV file is attached below.
    """
        # Make a mime object to define parts of the email
        msg = MIMEMultipart()
        msg["from"] = email_from
        msg["to"] = person
        msg["subject"] = subject
        # Attach th ebody of the message
        msg.attach(MIMEText(body, "plain"))
        # Define the file to attach
        filename = "Attendence.csv"
        # open the file in python as a binary
        attachment = open(filename, "rb")  # r for read and b for binary
        # Encode as base 64
        attachment_package = MIMEBase("application", "octet-stream")
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header(
            "content-Disposition", "attachment; filename= " + filename
        )
        msg.attach(attachment_package)
        # Cast as string
        text = msg.as_string()
        # Connect to the server
        bikash_server = smtplib.SMTP(smtp_server, smtp_port)
        bikash_server.starttls()
        bikash_server.login(email_from, password)
        print("Connected to server")

        print()
        print(f"Sending email to {person}")
        bikash_server.sendmail(email_from, person, text)
        print("Successfull")


send_emails(email_list)
