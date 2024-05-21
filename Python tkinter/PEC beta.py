import tkinter as tk
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


navegador = Firefox()

def opennav():

    url = "https://esustouros.com.br/"
    navegador.get(url)

def enterpag():
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
        element = WebDriverWait(navegador, 100).until(
            EC.visibility_of_element_located((By.CLASS_NAME,"css-1xc5sgu"))
        )
        # Clicar no elemento
        element.click()
        print("Elemento clicado com sucesso")
    except:
        print("Elemento não encontrado")


# Função a ser executada quando o primeiro botão é clicado
def clique_botao1():
    print("Botão 1 foi clicado")
    opennav()

# Função a ser executada quando o segundo botão é clicado
def clique_botao2():
    print("Botão 2 foi clicado")
    enterpag()


# Criando a janela principal
janela = tk.Tk()

# Criando os botões
botao1 = tk.Button(janela, text="Botão 1", command=clique_botao1)
botao2 = tk.Button(janela, text="Botão 2", command=clique_botao2)
botao1.pack()
botao2.pack()

# Iniciando o loop principal da aplicação
janela.mainloop()
