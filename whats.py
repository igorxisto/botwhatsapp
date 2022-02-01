import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromepath = r'./chromedriver.exe'
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\Igor\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(executable_path=chromepath, chrome_options=options)


driver.get('https://web.whatsapp.com')
time.sleep(20)
#definir contatos, grupos e mensagem
contato = ['Teste']
mensagem = 'se essa mensagem chegar pra ti é porque funcionou skks'

# Buscar contatos/grupos
def buscar_contato(contato):
   campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text" )]')
   time.sleep(3)
   campo_pesquisa.click()
   campo_pesquisa.send_keys(contato)
   campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text" )]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    
for contato in contato:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
    
    

