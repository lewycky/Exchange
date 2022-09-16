from urllib import response
from flask import render_template
import requests
import json, pickle
import csv
from flask import Flask

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


code=[   
{'currency': 'dolar amerykański', 'code': 'USD', 'bid': 4.6738, 'ask': 4.7682},
{'currency': 'dolar australijski', 'code': 'AUD', 'bid': 3.1489, 'ask': 3.2125},
{'currency': 'dolar kanadyjski', 'code': 'CAD', 'bid': 3.5488, 'ask': 3.6204},
{'currency': 'euro', 'code': 'EUR', 'bid': 4.67, 'ask': 4.7644},
{'currency': 'forint węgierski', 'code': 'HUF', 'bid': 0.011528, 'ask': 0.01176},
{'currency': 'frank szwajcarski', 'code': 'CHF', 'bid': 4.8598, 'ask': 4.958},
{'currency': 'funt szterling', 'code': 'GBP', 'bid': 5.407, 'ask': 5.5162},
{'currency': 'jen japoński', 'code': 'JPY', 'bid': 0.032708, 'ask': 0.033368},
{'currency': 'korona czeska', 'code': 'CZK', 'bid': 0.1905, 'ask': 0.1943},
{'currency': 'korona duńska', 'code': 'DKK', 'bid': 0.628, 'ask': 0.6406},
{'currency': 'korona norweska', 'code': 'NOK', 'bid': 0.4632, 'ask': 0.4726},
{'currency': 'korona szwedzka', 'code': 'SEK', 'bid': 0.4379, 'ask': 0.4467},
{'currency': 'SDR (MFW)', 'code': 'XDR', 'bid': 5.9977, 'ask': 6.1189}
]



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

   

