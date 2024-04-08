import os
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Inicialização do navegador
servico = Service()
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(service=servico, options=options)

# URL da página
url = 'https://www.spacemoney.com.br/ultimas-noticias'
driver.get(url)  

# Espera 1 segundo para a página carregar completamente
time.sleep(1)

# Maximiza a janela do navegador
driver.maximize_window()

# Encontra o botão 'adopt-reject-all-button' e clica nele, se estiver presente
try:
    mensagem = driver.find_element(By.ID, 'adopt-reject-all-button')
    mensagem.click()
except:
    pass

time.sleep(1)

# Encontra o link para a primeira notícia e clica nele
pagina_ultimas_noticia = driver.find_element(By.XPATH, '//*[@id="menu"]/div/ul[1]/li[2]/a')
pagina_ultimas_noticia.click()

time.sleep(1)

# Verifica se a página tem '#google_vignette' na URL e atualiza se tiver
if '#google_vignette' in driver.current_url:
    nova_url = driver.current_url.replace("#google_vignette","")
    driver.get(nova_url)

time.sleep(2)

# Encontra a primeira notícia
noticia_1 = driver.find_element(By.XPATH, '//*[@id="sectEditoria"]/div[2]/div[1]/a')
noticia_1.click()

time.sleep(1)

# Verifica se a notícia tem '#google_vignette' na URL e atualiza se tiver
if '#google_vignette' in driver.current_url:
    nova_url = driver.current_url.replace("#google_vignette","")
    driver.get(nova_url)

noticia_1 = driver.find_element(By.XPATH, '//*[@id="sectEditoria"]/div[2]/div[1]/a')
noticia_1.click()

# Coleta o texto da primeira notícia
paragrafos_noticia_1 = driver.find_elements(By.XPATH,'//*[@id="sc_noticia2"]/header/h1 | //*[@id="sc_noticia"]/article[1]//p | //*[@id="sc_noticia"]/article[1]/p[2] | //*[@id="sc_noticia"]/article[1]/p[3] | //*[@id="sc_noticia"]/article[1]/p[4] | //*[@id="sc_noticia"]/article[1]/p[5]')

# Espera 2 segundos para garantir que o texto seja totalmente carregado
time.sleep(2)

# Escreve o texto do artigo em um arquivo de texto
with open('artigo_noticia_1.txt', 'w', encoding='utf-8') as arquivo:
    for paragrafo in paragrafos_noticia_1:
        arquivo.write(paragrafo.text + '\n')

# Espera 1 segundo para garantir que o arquivo seja salvo
time.sleep(1)

# Baixa o arquivo para o computador
os.system('start artigo_noticia_1.txt')

