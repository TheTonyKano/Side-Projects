import requests
startURL = "https://en.wikipedia.org/wiki/Tesla,_Inc."

downloaded_html = requests.get(startURL)

soup = BeautifulSoup(downloaded_html.text)

with open('downloaded.html', 'w') as file:
    file.write(soup.prettify())