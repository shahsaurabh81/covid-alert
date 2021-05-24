import requests, hashlib, pathlib
from pprint import pprint as pp
#from datetime import date
import arrow

#today = str(date.today())
#print(today)

today = arrow.now()
print(today)

nextDay = today.shift(days=1).format('DD-MM-YYYY')
print(nextDay)

pincode = 461001


#URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=461001&date=24-05-2021"

#response = requests.get(URL, headers={
#    "accept": "application/json",
#    "Accept-Language": "en_US",
#    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
#})

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

proceed = False

if (proceed):
    print(proceed)


    # just some random token
    token="U2FsdGVkX1+TPSV7/E3PENx8ObiaQ9mIov/NO0Ry1mt5O8Awl1Ix+kX68wcBDbBTODj4Ejy3KkeW3n8ZqYhlqA=="

    URL = "https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP"
    response = requests.post(URL, json={
        "mobile": "1234567890",
        "secret": token
    }, headers={
        "accept": "application/json",
        "Accept-Language": "en_US",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    })

    print(response)

    otp=str(input("Enter OTP: "))
    otpHash=hashlib.sha256(otp.encode()).hexdigest()

    URL = "https://cdn-api.co-vin.in/api/v2/auth/validateMobileOtp"
    response = requests.post(URL, json={
        "otp": otpHash,
        "txnId": response.json()['txnId']
    }, headers={
        "accept": "application/json",
        "Accept-Language": "en_US",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    })

    # the response has the bearer token
    bearer_token=response.json()['token']


    URL = "https://cdn-api.co-vin.in/api/v2/appointment/beneficiaries"
    response = requests.get(URL, headers={
        "accept": "application/json",
        "Accept-Language": "en_US",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "authorization": "Bearer {}".format(bearer_token)
    })

    # printing the beneficiaries list
    print(response.json())


print("end-processing")
