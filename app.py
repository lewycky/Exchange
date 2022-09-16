
from locale import currency
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

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        code = data.get('code')
        amount = data.get('amount')
        ask = data.get('ask')
        for rate in rates:
            if rate['code'] == request.form['codes']:
                wynik= round((float((rate['ask'])) * float(amount)), 2)
    return render_template("index.html", codes=codes, data=data, result=wynik )


if __name__ == "__main__":
    app.run(debug=True)   