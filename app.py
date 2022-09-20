
from locale import currency
from unittest import result
import requests
import csv
from flask import Flask, render_template, request, redirect

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0].get('rates')

app = Flask(__name__)

def get_codes():
    codes = []
    for data in rates:
        codes.append(data.get('code'))
    return sorted(codes)

codes = get_codes()

with open('rates.csv', 'w') as csvfile:
    fieldnames = ['currency', 'code', 'bid', 'ask']
    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rates)


rates = [{'currency': 'dolar amerykański', 'code': 'USD', 'bid': 4.5998, 'ask': 4.6928},
{'currency': 'dolar australijski', 'code': 'AUD', 'bid': 3.1675, 'ask': 3.2315},
{'currency': 'dolar kanadyjski', 'code': 'CAD', 'bid': 3.5468, 'ask': 3.6184},
{'currency': 'euro', 'code': 'EUR', 'bid': 4.6564, 'ask': 4.7504},
{'currency': 'forint węgierski', 'code': 'HUF', 'bid': 0.011744, 'ask': 0.011982},
{'currency': 'frank szwajcarski', 'code': 'CHF', 'bid': 4.8245, 'ask': 4.9219},
{'currency': 'funt szterling', 'code': 'GBP', 'bid': 5.3763, 'ask': 5.4849},
{'currency': 'jen japoński', 'code': 'JPY', 'bid': 0.032255, 'ask': 0.032907},
{'currency': 'korona czeska', 'code': 'CZK', 'bid': 0.1899, 'ask': 0.1937},
{'currency': 'korona duńska', 'code': 'DKK', 'bid': 0.6262, 'ask': 0.6388},
{'currency': 'korona norweska', 'code': 'NOK', 'bid': 0.4678, 'ask': 0.4772},
{'currency': 'korona szwedzka', 'code': 'SEK', 'bid': 0.4389, 'ask': 0.4477},
{'currency': 'SDR (MFW)', 'code': 'XDR', 'bid': 6.0346, 'ask': 6.1566}
]

codes = ["USD", "AUD", "CAD", "EUR", "HUF", "CHF", "GBP", "JPY", "CZK", "DKK", "NOK", "SEK", "XDR" ]



@app.route("/home", methods=["GET", "POST"])
def home():
    score = None
    if request.method == "POST":
        amount = request.form['amount']
        for rate in rates:
            if rate['code'] == request.form['codes']:
                  score = round((float((rate['ask'])) * float(amount)), 2)
    return render_template("index.html", codes=codes, data=data, result=score )


if __name__ == "__main__":
    app.run(debug=True)
       