import smtplib, ssl
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Test message")
msg['Subject'] = 'This is a test message'
msg['From'] = "maccam6@gmail.com"
msg['To'] = "martin.carufel@dental-wings.com"

port = 465  # For SSL
# # password = input("Type your password and press enter: ")
password = "18,Mac&Amo"
# # Create a secure SSL context
context = ssl.create_default_context()
# sender_email = "maccam6@gmail.com"
# receiver_email = "martin.carufel@dental-wings.com"
# message = msg = '''\\
#          ... From: Me@my.org
#          ... Subject: testin'
#          ...
#          ... This is a test '''
#
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("maccam6@gmail.com", password)
    result = server.send_message(msg)
    print(result)
#     # TODO: Send email here