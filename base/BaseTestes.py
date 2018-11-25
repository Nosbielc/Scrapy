import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.uol.com.br/")

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

soup.find('esporte')

print(soup)

#link = soup.find_all('div', attrs={'class':'widget-horizontal-left-box '})
link = soup.find_all('div')

print(link.__len__())
