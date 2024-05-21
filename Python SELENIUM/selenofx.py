from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://esustouros.com.br/"

navegador = Firefox()

navegador.get(url)

xusuario = '/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[1]/form/div/div[1]/div/div[1]/div/div/input'
user = navegador.find_element('xpath', xusuario)
user.send_keys("10837388449")

senha = navegador.find_element(By.NAME,"password")
senha.send_keys("bolsonaro2024")


botao = navegador.find_element(By.CLASS_NAME,"css-1mc6ylg")
botao.click()

try:
    # Esperar até que o elemento seja visível
    element = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "css-1jy51ie"))
    )
    # Clicar no elemento
    element.click()
    print("Elemento clicado com sucesso")
except:
    print("Elemento não encontrado")

try:
    # Esperar até que o elemento seja visível
    element = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME,"css-1xc5sgu"))
    )
    # Clicar no elemento
    element.click()
    print("Elemento clicado com sucesso")
except:
    print("Elemento não encontrado")

# botao3 = navegador.find_element(By.CLASS_NAME,"css-1jy51ie")
# botao3.click()


# Esqueleto de espera dos elementos
# try:
#     elemento = WebDriverWait(navegador,100).until(EC.visibility_of_element_located((By.CLASS_NAME,"Name class")))
#     elemento.click()
#     print("Achou o elemento e clicou nele")
# except:
#     print("Não achou o elemento, e não clicou")