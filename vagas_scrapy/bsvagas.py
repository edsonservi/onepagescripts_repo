from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def detalhar(link):

    options = Options()
    options.add_argument('--headless')
    janela = webdriver.Chrome(options=options)
    janela.get(link)
    with open("vagas.txt", 'r', encoding='utf-8') as arquivo:
        arqui = arquivo.readlines()
    id = janela.find_element(By.TAG_NAME, "article").get_property("id")
    controle = False
    for frase in arqui:
        if id in frase:
            controle = True
    if controle == False:
        titulo = janela.find_element(By.TAG_NAME, 'h1').text
        meta = janela.find_element(By.CLASS_NAME, 'job-listing-meta')
        empresa = janela.find_element(By.CLASS_NAME, 'company').text
        tipo = meta.find_element(By.CLASS_NAME, 'job-type').text
        local = meta.find_element(By.CLASS_NAME, 'location').text
        try:
            salario = meta.find_element(By.CLASS_NAME, 'salary').text
        except:
            salario = 0
        post = meta.find_element(By.CLASS_NAME, 'date-posted').text
        texto = janela.find_element(By.CLASS_NAME, "job_description").text
        texto = texto.replace("\n", " =-= ")
        detail = janela.find_element(By.CLASS_NAME, "application_details")
        detail = detail.find_element(By.TAG_NAME, "a").get_property("href")
        mensagem = f"\n'{id}', '{titulo}', '{link}', '{empresa}', '{tipo}', '{local}', " \
                   f"'{salario}', '{post}', '{texto}', '{detail}';"
        with open("vagas.txt", 'a', encoding='utf-8') as arquivo:
            arquivo.write(mensagem)
            print("Vaga cadastrada!")
    else:
        print(f'Vaga já cadastrada!')


detalhar("https://vagas.sc/vaga/kebook-sao-jose-social-media-19/")
detalhar("https://vagas.sc/vaga/kebook-sao-jose-auxiliar-financeiro-8/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-assistente-comercial-backoffice-home-office/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-36-assistente-financeiro-4/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-33-vendedor-5/")
detalhar("https://vagas.sc/vaga/empresa-palhoca-sc-36-assistente-de-logistica-2/")
detalhar("https://vagas.sc/vaga/empresa-palhoca-sc-36-assistente-de-qualidade/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-36-vendedor-interno-2/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-33-auxiliar-de-vendas-interno/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-assistente-de-relacionamento/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-analista-de-relacionamento-2/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-analista-de-relacionamento-ao-cliente/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-auxiliar-administrativo-12/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-33-auxiliar-de-producao-4/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-36-assistente-de-pos-vendas/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-33-auxiliar-de-producao-noturno-2/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-vendedora-5/")
detalhar("https://vagas.sc/vaga/empresa-palhoca-sc-33-auxiliar-de-limpeza-3/")
detalhar("https://vagas.sc/vaga/empresa-palhoca-sc-33-auxiliar-de-logistica-3/")
detalhar("https://vagas.sc/vaga/empresa-palhoca-sc-33-auxiliar-de-cozinha-2/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-33-promotor-de-vendas-cosmeticos/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-33-executivo-comercial/")
detalhar("https://vagas.sc/vaga/empresa-palhoca-sc-33-logistica-conferente/")
detalhar("https://vagas.sc/vaga/supermercado-sao-jose-sc-33-operador-de-caixa-2/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-33-auxiliar-de-alimentacao-padaria-confeitaria-cozinha/")
detalhar("https://vagas.sc/vaga/empresa-palhoca-sc-33-auxiliar-de-logistica-2/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-36-vendedora-5/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-atendente-comercial-2/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-36-vendedora-4/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-36-analista-comercial/")
detalhar("https://vagas.sc/vaga/loja-de-materiais-de-construcao-sao-jose-sc-36-vendedor-meio-periodo/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-36-motorista-de-caminhao/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-36-ajudante-operacional-2/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-auxiliar-de-cozinha-28/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-33-assistente-administrativo-de-vendas/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-garcom-8/")
detalhar("https://vagas.sc/vaga/restaurante-florianopolis-sc-33-lavador-de-pratos-2/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-garcom-7/")
detalhar("https://vagas.sc/vaga/empresa-sao-jose-sc-33-almoxarife-de-obras/")
detalhar("https://vagas.sc/vaga/empresa-florianopolis-sc-33-auxiliar-de-contas-a-receber/")
