from twilio.rest import Client
from twilio import rest

# Your Account SID from twilio.com/console - found in General Settings
account_sid = "***************************"
# Your Auth Token from twilio.com/console - found in General Settings
auth_token  = "***************************"

#client = Client(account_sid, auth_token)
client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+35799******",#Your phone number
    from_="+***********",#Found in "All products and services/Active Numbers"
    body="Hello from Python, Luke!")

print(message.sid)
