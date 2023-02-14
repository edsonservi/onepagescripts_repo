from bs4 import BeautifulSoup
soup = BeautifulSoup('https://vagas.sc/lista-de-vagas/', 'html.parser')
print(soup.prettify())
