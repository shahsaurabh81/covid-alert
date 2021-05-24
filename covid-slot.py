import requests, hashlib, pathlib
from pprint import pprint as pp
import arrow
import json
#import send_sms

today = arrow.now()
print(today)

nextDay = today.shift(days=1).format('DD-MM-YYYY')
print(nextDay)

pincode = 461001

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

mydict = json.loads(response.text)
print(type(mydict))

#print(list(mydict.keys())[list(mydict.values()).index(574478)])


smsFlag = False

#if (smsFlag):
#    send_sms


print("exit-processing")
