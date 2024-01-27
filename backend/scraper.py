import requests
from bs4 import BeautifulSoup

def get_drug_info(name):
    url = f'https://drugs.com/{name}.html'
    resp = requests.get(url)
    soup = BeautifulSoup('html.parser', resp.content)
    soup.find()