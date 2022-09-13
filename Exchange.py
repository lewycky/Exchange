from urllib import response
import requests
import json, pickle
import csv


response = requests.get("https://api.nbp.pl/api/exchangerates/tables/C?format=json")

data = response.json()
data_as_jason=json.dumps(data)


rates=[]

for item in data:
    rates.append(item['rates'])



with open('file.csv', 'w') as f:
    for row in rates:
        for x in row:
            f.write(str(x)+ ';')
            f.write('\n')





   








