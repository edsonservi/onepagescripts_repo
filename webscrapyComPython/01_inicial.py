import requests
from bs4 import BeautifulSoup

response = requests.get("https://vagas.sc/lista-de-vagas/")
# response = requests.get("https://g1.globo.com/")
content = response.content
site = BeautifulSoup(content, 'html.parser')
# print(site.prettify())
# nota = site.find('div', attrs={'class': 'bstn-hl-wrapper'})
nota = site.find('div', attrs={'class': 'container'})
print(nota.prettify())
