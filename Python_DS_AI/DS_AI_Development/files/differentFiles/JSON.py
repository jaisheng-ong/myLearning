"""
        JSON File
        - .dump() -- use to write to json file
        - .dumps() -- Convert to JSON string
        - .load() -- Read from file

WRITING (Serialization):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Python Dictionary              JSON File
┌─────────────────┐           ┌──────────────────┐
│ person = {      │           │ {                │
│   'name': 'Mark'│  dump()   │   "name": "Mark" │
│   'age': 27     │  ──────>  │   "age": 27      │
│ }               │           │ }                │
└─────────────────┘           └──────────────────┘


READING (Deserialization):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JSON File                      Python Dictionary
┌──────────────────┐          ┌─────────────────┐
│ {                │          │ person = {      │
│   "name": "Mark" │  load()  │   'name': 'Mark'│
│   "age": 27      │  ──────> │   'age': 27     │
│ }                │          │ }               │
└──────────────────┘          └─────────────────┘
"""

import json

with open('gdp_data.json', 'r') as openfile:
    json_object = json.load(openfile)

print(json_object)

person = {
    'first_name' : 'Victoria',
    'last_name' : 'Lai',
    'age' : 22,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}


with open('person.json', 'w') as f: #convert dict -> JSON and writes to file
    json.dump(person, f)

# Convert to JSON string with nice formatting (4-space indentation)
json_object = json.dumps(person, indent=4)

# Write the string to file
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print(json_object)

"""
            Reading JSON
            - json.load() -- read from file
"""

with open('sample.json', 'r') as openFile:
    json_object = json.load(openFile)       # reads file and converts JSON -> Python dict

print(json_object)
print("Type of object: ", type(json_object))

print("First Name:", json_object['first_name'])
print("Last Name: ", json_object['last_name'])
print("Age:", json_object['age'])
print("City:", json_object['address']['city'])