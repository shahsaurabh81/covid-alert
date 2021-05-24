import requests, hashlib, pathlib
from pprint import pprint as pp
import arrow
import json
#import send_sms
from twilio.rest import Client


today = arrow.now()
print(today)

nextDay = today.shift(days=1).format('DD-MM-YYYY')
print(nextDay)

pincode = 461001

#payload = {'pincode': pincode, 'date': '24-05-2021'}
payload = {'pincode': pincode, 'date': nextDay}

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"

response = requests.get(URL, params=payload, headers={
    "accept": "application/json",
    "Accept-Language": "en_US",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
})

print("here-1")
print(response)
print("here-2")
print(response.text)
print("here-3")
pp(response.json())
print("here-4")
print(response.json())
print("here-5")

mydictionary = json.loads(response.text)
print(type(mydictionary))

#print(list(mydict.keys())[list(mydict.values()).index(574478)])

pp(mydictionary)
print(type(mydictionary))
print(len(mydictionary))

#print(mydictionary.get('sessions')[0])
#print(mydictionary.get('sessions')[1])
print(mydictionary.keys())
print(mydictionary.values())
mydictvalues = len(mydictionary.values())
print(mydictvalues)

#print(mydictionary.get('sessions')[0]['center_id'])

print('before-loop')

smsFlag = False

for row, column in mydictionary.items():
    print(row)
    for center in column:
        print(center)
        print(center.get('center_id'))
        smsFlag = True


def send_sms(smsFlag):
    if (smsFlag):
        print('inside-send-sms-function')
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



if (smsFlag):
    print('execute-send_sms')

    send_sms(smsFlag)

    print('done-sending-sms')




print("exit-processing")

