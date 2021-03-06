import json 
x = """{
    "name": "Ravi Mevcha", 
    "country": "India", 
    "city": "Mumbai", 
    "current_company": "Mahindra Rise", 
    "education": [
        {"Degree": "MBA", "School": "International Institute of Information Technology (I2IT), Pune"},
        {"Degree": "B.E.", "School": "Gujarat University"}
    ], 
    "socials": [
        {"social": "Twitter", "title": "Ravi Mevcha (@ravimevcha) / Twitter", "link": "https://twitter.com/ravimevcha"},
        {"social": "Instagram", "title": "Ravi Mevcha - Product Management Lead - LinkedIn India", "link": "https://in.linkedin.com/in/ravimevcha"},
        {"social": "Facebook", "title": "Ravi Mevcha - Product Management Lead - LinkedIn India", "link": "https://in.linkedin.com/in/ravimevcha"}
    ]
}"""

y = json.loads(x)

import csv

fieldnames = ['name','country','city','current_company', 'education', 'socials']

with open('output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(y)