# import smtplib
# import ssl

# # Set up port 
# smtp_port=587                #Stanndard secure SMTP port
# smtp_server="smtp.gmail.com" # google smtp server


# email_from= "bikashchamua555@gmail.com"
# email_to= "bikashchamua555@gmail.com"

# password="eaguhgnopcgruokc"

# # content of message

# message="Hi sir, How are you doing"

# try:
#     simple_email_context=ssl.create_default_context()
#     TIE_server=smtplib.SMTP(smtp_server,smtp_port)
#     TIE_server.starttls(context=simple_email_context)
#     TIE_server.login(email_from,password)
#     print("Connected to server")

#     print()
#     print(f"Sending email to {email_to}")
#     TIE_server.sendmail(email_from,email_to,message)
#     print("Successfull")
# except Exception as es:
#     print(es)

#     # finally:
#     #     TIE_server.quit()

from with_attachment_email import send_emails

send_emails()