from pprint import pprint as pp
import json

#mydictionary = dict({'sessions': [{'center_id': 574478, 'name': 'Govt SNG School HBAD 45', 'address': 'Govt SNG School HBAD 45', 'state_name': 'Madhya Pradesh', 'district_name': 'Hoshangabad', 'block_name': 'HOSHANGABAD', 'pincode': 461001, 'from': '09:00:00', 'to': '17:00:00', 'lat': 22, 'long': 77, 'fee_type': 'Free', 'session_id': '037d3cef-97e8-4f2f-bb05-69e58546d399', 'date': '24-05-2021', 'available_capacity_dose1': 0, 'available_capacity_dose2': 20, 'available_capacity': 20, 'fee': '0', 'min_age_limit': 45, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM']}, {'center_id': 561357, 'name': 'Govt Girl SCHOOL H BAD 18', 'address': 'Govt Girl SCHOOL H BAD 18', 'state_name': 'Madhya Pradesh', 'district_name': 'Hoshangabad', 'block_name': 'HOSHANGABAD', 'pincode': 461001, 'from': '09:00:00', 'to': '17:00:00', 'lat': 22, 'long': 77, 'fee_type': 'Free', 'session_id': 'bb950fa4-a6d6-4714-81fb-4a9115c7534f', 'date': '24-05-2021', 'available_capacity_dose1': 0, 'available_capacity_dose2': 0, 'available_capacity': 0, 'fee': '0', 'min_age_limit': 18, 'vaccine': 'COVISHIELD', 'slots': ['09:00AM-11:00AM', '11:00AM-01:00PM', '01:00PM-03:00PM', '03:00PM-05:00PM']}]})
mydictionary = dict({'sessions': []})

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


#for row, column in mydictionary.items():
#    print(mydictionary.get('sessions'))
#    print('ID: ', row)
#
#    for key in column:
#        print(mydictionary.get('sessions')[key]['center_id'])

print('before-loop')

for row, column in mydictionary.items():
    print(row)
    for center in column:
        print(center)
        print(center.get('center_id'))


