import requests
import re
from bs4 import BeautifulSoup

def getsteamlink(query:str):
    searchquery = f'{query.replace(' ','+')}+on+Steam'
    x = requests.get(f'https://www.google.com/search?hl=en&tbm=isch&q={searchquery}')
    soup = BeautifulSoup(x.text, 'html.parser')
    steamlinks = soup.find_all('a')
    for steamlink in steamlinks:
        href = steamlink.get('href')
        if 'url?q=' in href and 'https://store.steampowered.com/app/' in href:
            return href[7:]

def getimglink(url:str):
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        if 'store_item_assets/steam/apps/' in image.get('src'):
            return image.get('src')

honkai = 'Honkai Impact 3rd'
wukong = 'Black Myth: Wukong'
print(getimglink(getsteamlink(wukong)))