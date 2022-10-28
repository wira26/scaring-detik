from operator import index
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app =  Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/detik-populer')
def detik_populer():
    url = requests.get('https://www.detik.com/terpopuler')

    soup = BeautifulSoup(url.text, "html.parser")

    populer = soup.find(attrs={'class':'grid-row list-content'})

    titles = populer.findAll(attrs={'class':'media__title'})
    images = populer.findAll(attrs={'class':'media__image'})

    return render_template('detik.html', images=images)

@app.route('/idr-rates')
def idr_rates():
    url = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = url.json()
    return render_template('idr.html', datas =json_data.values())



if __name__ == '__main__':
    app.run(debug=True)