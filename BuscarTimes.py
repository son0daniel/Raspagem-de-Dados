#Importação de bibliotecas
from time import sleep #Da bilioteca time importar apenas a função 'sleep'
from bs4 import BeautifulSoup #Importar BeautifulSoup para trabalhar com HTML
#Importação do Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://ge.globo.com/sp/futebol/paulista-segunda-divisao/'
op = webdriver.ChromeOptions()
op.add_argument('headless') #Argumento que impede que o navegador seja aberto e trabalhe silenciosamente
driver = webdriver.Chrome('./chromedriver.exe', options=op) #Pega o webdriver do Chrome localizado na pasta
driver.get(url) #Acessa a URL
sleep(.5) #Tempo suficiente para renderizar JavaScript da maioria das páginas
pagina = driver.page_source #Pega o HTML da página renderizada
driver.close() #Fecha o navegador
site_html = BeautifulSoup(pagina, 'html.parser') #Converte o contéudo da página em HTML através do BeautifulSoup
times_tabela = site_html.find_all('strong', attrs={'class': 'classificacao__equipes classificacao__equipes--nome'}) #Pega todo contéudo dentro dos parâmetros (que são tags do HTML) solicitados
times_r = open("times.txt", 'r', encoding='utf8') #Cria uma varíavel de LEITURA para o bloco de notas times.txt
times_a = open("times.txt", 'a', encoding='utf8') #Cria uma varíavel de ESCRITA para o mesmo bloco de notas

#Criação de listas
r = [] #Lista do conteúdo do bloco de notas
for x in times_r:
    r.append(str(x)) #Adiciona contéudo do bloco de notas à variável em um loop
times_r.close() #Fecha a variável de leitura do bloco de notas

a = [] #Lista do conteúdo da tabela que está na URL do ge.globo.com
for x in times_tabela:
    a.append(str(x.text + "\n")) #Adiciona conteúdo do site à variável

for x in a:
    if x not in r: #Pergunta se um time não está presente no bloco de notas
        times_a.write(x) #Se não estiver presente, o time é adicionado
    else:
        print(x.replace("\n", "") + " já existe") #Caso esteja presente, será informado
times_a.close() #Fecha a variável de escrita

#ORDEM ALFABÉTICA
times_r = open("times.txt", 'r', encoding='utf8') #Abre novamente a variável de leitura

#Repete o processo de adicionar conteúdo oriundo do bloco de notas
r = []
for x in times_r:
    r.append(str(x))
times_r.close()
r.sort() #Orderna o conteúdo em ordem alfabética

times_w = open("times.txt", 'w', encoding='utf8') #Cria uma variável que SOBRESCREVE completamente o conteúdo do bloco de notas
#Reescreve o conteúdo do bloco de notas com ordem alfabética
for x in r:
    times_w.write(str(x))