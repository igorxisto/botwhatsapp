#importar bibliotecas

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\Igor\\AppData\\Local\\Google\\Chrome\\User Data")




#Navegar até o whatsapp web
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)
driver.get('https://web.whatsapp.com')
time.sleep(15)
#definir contatos, grupos e mensagem
contatos =['Teste']
mensagem = ['Testando, se você receber essa mensagem, é o meu Bot']

# Buscar contatos/grupos
def buscar_contato(contato):
   campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text" )]')
   time.sleep(3)
   campo_pesquisa.click()
   campo_pesquisa.send_keys(contatos)
   campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text" )]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
    



# Enviar mensagens 
# campo de pesquisa -> copyable-text selectable-text
# campo de mensagem privada -> copyable-text selectable-text