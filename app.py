#from webbrowser import get
#importando
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


navegador= webdriver.Chrome(ChromeDriverManager().install())
#celecionando a pagina
navegador.get('https://www.google.com.br')
#escrever na barra de pesquisa
navegador.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação de dolar')
#pesquisar dando enter
navegador.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
time.sleep(100)