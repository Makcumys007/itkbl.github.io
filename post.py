
from exchangelib import Configuration, GSSAPI, SSPIpin
from exchangelib import Credentials, Configuration, Account, DELEGATE, GSSAPI, SSPI
from exchangelib import Message, Mailbox
from exchangelib.protocol import BaseProtocol
BaseProtocol.USERAGENT = "Auto-Reply/0.1.0"

import os

LOGIN_PASSWORD = os.getenv("PASSWORD")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_USER = os.getenv("LOGIN_USER")    
SMTP_SERVER = os.getenv("SMTP_SERVER") 
RECEPIENT_EMAIL = os.getenv("RECEPIENT_EMAIL")


credentials = Credentials(username=LOGIN_USER, password=LOGIN_PASSWORD)

config = Configuration(auth_type=SSPI)
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




