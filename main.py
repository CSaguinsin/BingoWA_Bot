from twilio.rest import Client
from dotenv import load_dotenv
import os



load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)
message = client.messages.create(
    body='Hello this is Bingo Assistant!',
    to='+18777804236',
    from_='+12076402679'  
)
print(message.sid)