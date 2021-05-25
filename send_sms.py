# Download the helper library from https://www.twilio.com/docs/python/install
#import os
from twilio.rest import Client

print("inside-send-sms-module")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']

account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body='Twilio test SMS',
    from_='+12093439074',
    to='+14168320235'
    #    to='+919827507557'
)

print(message.sid)

print("exit-send-sms-module")
