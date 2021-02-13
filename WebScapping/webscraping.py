import requests
from bs4 import BeautifulSoup

startURL = "https://en.wikipedia.org/wiki/Tesla,_Inc."

downloaded_html = requests.get(startURL)

soup = BeautifulSoup(downloaded_html.text, 'html.parser')

with open('downloaded.html', 'w', encoding="utf-8") as file:
    file.write(soup.prettify())