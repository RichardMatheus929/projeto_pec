from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://esustouros.com.br/")

xusuario = '/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[1]/form/div/div[1]/div/div[1]/div/div/input'
# xusuario = '/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[1]/form/div/div[1]/div/div[1]/div/div/input
xsenha = '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/form/div/div[2]/div/div/div/div/div/div/input'


navegador.find_element('xpath', xusuario).send_keys("10837388449")

navegador.find_element('xpath',xsenha).send_keys("BOLSONARO2024")

time.sleep(1000)


