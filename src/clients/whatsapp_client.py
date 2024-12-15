import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class Whatsapp_Client:
    def __init__(self):
        self.ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
        self.AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
        self.TWILIO_NUM = os.getenv("TWILIO_PRIVATE_NUM")
        self.TO_NUM = os.getenv("TO_NUM")
        self.client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)

    def custom_message(self,message):
        message = self.client.messages.create(
            body=f"{message}", from_=f"{self.TWILIO_NUM}", to=f"{self.TO_NUM}")
