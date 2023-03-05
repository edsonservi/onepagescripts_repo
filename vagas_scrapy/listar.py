from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
# options.add_argument('--start-maximized')
options.add_argument('--headless')
nav = webdriver.Chrome(options=options)
nav.get('https://vagas.sc/lista-de-vagas/')
n = 1
while True:
    pagina = nav.find_element(By.CLASS_NAME, 'job-manager-pagination')
    try:
        contador = pagina.find_element(By.LINK_TEXT, "→")
    except:
        divVagas = nav.find_element(By.CLASS_NAME, 'job_listings')
        vagas = divVagas.find_elements(By.TAG_NAME, "article")
        for artigo in vagas:
            local = artigo.find_element(By.CLASS_NAME, "google_map_link").text
            if local == "São José, SC" or local == "Palhoça, SC" or local == "Florianópolis, SC":
                tipo = artigo.find_element(By.CLASS_NAME, "job-type").text
                if tipo == "EFETIVO" or tipo == "N/I":
                    link = artigo.find_element(By.TAG_NAME, "a").get_property("href")
                    print(link)
        print("FIM")
        break
    else:
        divVagas = nav.find_element(By.CLASS_NAME, 'job_listings')
        vagas = divVagas.find_elements(By.TAG_NAME, "article")
        for artigo in vagas:
            local = artigo.find_element(By.CLASS_NAME, "google_map_link").text
            if local == "São José, SC" or local == "Palhoça, SC" or local == "Florianópolis, SC":
                tipo = artigo.find_element(By.CLASS_NAME, "job-type").text
                if tipo == "EFETIVO" or tipo == "N/I":
                    link = artigo.find_element(By.TAG_NAME, "a").get_property("href")
                    print(link)
        contador.send_keys(Keys.ENTER)
print("FINAL")
