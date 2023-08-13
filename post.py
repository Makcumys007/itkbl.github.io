from exchangelib import Credentials, Configuration, Account, DELEGATE, GSSAPI, SSPI, Build, NTLM, Version, IMPERSONATION, FaultTolerance
from exchangelib import Message, Mailbox



import os

LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_USER = os.getenv("LOGIN_USER")    
SMTP_SERVER = os.getenv("SMTP_SERVER") 
RECEPIENT_EMAIL = os.getenv("RECEPIENT_EMAIL")




credentials = Credentials(username=LOGIN_USER, password=LOGIN_PASSWORD)
config = Configuration(server=SMTP_SERVER, credentials=credentials)



account = Account(
    primary_smtp_address=LOGIN_EMAIL,
    config=config,
    autodiscover=True,
    access_type=DELEGATE,
)

m = Message(
    account=account,
    folder= account.sent,
    subject="Hello Message From Bot",
    body="Hello! This is test message from bot",
    to_recipients=[Mailbox(email_address=RECEPIENT_EMAIL)],
)
m.send_and_save()




