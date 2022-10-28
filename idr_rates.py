import requests

# url = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.4159050304326e-5,"date":"Wed, 26 Oct 2022 23:55:01 GMT","inverseRate":15586.265620465},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.3904517531793e-5,"date":"Wed, 26 Oct 2022 23:55:01 GMT","inverseRate":15648.345979648}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['data'])
    print(data['inverseRate'])