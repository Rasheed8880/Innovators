import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.get_text()
    except:
        return "Could not fetch link content"