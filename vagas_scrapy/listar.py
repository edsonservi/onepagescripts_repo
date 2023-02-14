from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--start-maximized')
nav = webdriver.Chrome(options=options)

nav.get('https://vagas.sc/lista-de-vagas/')
print(nav)
