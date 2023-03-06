with open("vagas.csv", 'r') as arquivo:
    print(arquivo.read())
"""
# 1. cria o arquivo
f = open('vagas.csv', 'rb', newline='', encoding='utf-8')
x = f.read()
# 2. cria o objeto de gravação
print(x)

# 3. grava as linhas

for i in range(15):
    f.write(f"\n{i}")
# Recomendado: feche o arquivo
f.close()
# LER UM REGISTRO E SALVAR EM CSV
# LER A PAGINA ATUAL E PASSAR OS LINKS PRA FUNÇAO ANTERIOR
# PERCORRER A PAGINAÇÂO

"""
