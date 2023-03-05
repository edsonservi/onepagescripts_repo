from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def detalhar(link):
    options = Options()
    options.add_argument('--headless')
    janela = webdriver.Chrome(options=options)
    janela.get(link)
    titulo = janela.find_element(By.TAG_NAME, 'h1').text
    meta = janela.find_element(By.CLASS_NAME, 'job-listing-meta')
    empresa = janela.find_element(By.CLASS_NAME, 'company').text
    tipo = meta.find_element(By.CLASS_NAME, 'job-type').text
    local = meta.find_element(By.CLASS_NAME, 'location').text
    salario = meta.find_element(By.CLASS_NAME, 'salary').text
    post = meta.find_element(By.CLASS_NAME, 'date-posted').text
    texto = janela.find_element(By.CLASS_NAME, "job_description").text
    detail = janela.find_element(By.CLASS_NAME, "application_details")
    detail = detail.find_element(By.TAG_NAME, "a").get_property("href")

    print("*" * 30)
    print(titulo)
    print(link)
    print(f"Empresa: {empresa}")
    print(f"Tipo: {tipo}")
    print(f"Local: {local}")
    print(f"Salario: {salario}")
    print(f"{post}")
    print(f"\n{texto}\n")
    print(f'Link: {detail}')
    print("*" * 30)


detalhar("https://vagas.sc/vaga/kebook-sao-jose-social-media-19/")
