from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Seleno:
    def __init__(self):

        servico = Service(ChromeDriverManager().install())

        navegador = webdriver.Chrome(service=servico)

        



        pass


Seleno()