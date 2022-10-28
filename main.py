import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.detik.com/terpopuler')

soup = BeautifulSoup(url.text, "html.parser")

populer = soup.find(attrs={'class':'grid-row list-content'})

titles = populer.findAll(attrs={'class':'media__title'})

images = populer.findAll(attrs={'class':'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])

# print(titles)