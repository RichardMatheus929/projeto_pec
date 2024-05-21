from tkinter import *
from tkinter import ttk
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui as pg

# Aqui onde ficarão os métodos

# TACICLEZIA
# TACICLEZIA0496

def enteruser():
    navegador.get('https://plenassessoria.com.br/irb/touros/backend/web/index.php?r=site%2Flogin')
    navegador.find_element(By.XPATH,'//*[@id="loginform-username"]').send_keys('TACICLEZIA')
    navegador.find_element(By.XPATH,'//*[@id="loginform-password"]').send_keys('TACICLEZIA0496')
    navegador.find_element(By.XPATH,'/html/body/div/div[2]/form/div[3]/div[2]/button').click()

def taciclezia():
    # Clica no profissional e digita tarciclezia
    elementoprofissional = navegador.find_element(By.XPATH,'/html/body/div[1]/div[1]/section[2]/div/div/form/div[3]/span')
    elementoprofissional.send_keys('tarciclezia')
    # Clica no nome 
    tarciclezia = navegador.find_element(By.XPATH,'//*[@id="select2-producao-medicoid-results"]')
    tarciclezia.click()
    # Clica no procedimento e digita
    elementoprocedimento = navegador.find_element(By.XPATH,'/html/body/div[1]/div[1]/section[2]/div/div/form/div[7]/span')
    elementoprocedimento.send_keys('orientação de higiene bucal')
    # Clica na orientação
    orientacaohigiene = navegador.find_element(By.XPATH,'//*[@id="select2-producao-procedimentoid-results"]')
    orientacaohigiene.click()
    # Adiciona 1 em qntd
    navegador.find_element(By.XPATH,'//*[@id="producao-quantidade"]').send_keys('1')

    


# ---- Interface gráfica a partir daqui ----
        
janela = Tk()
janela.title("PEC_version001")
janela.geometry("300x150+100+200")

navegador = Firefox()

texto = Label(janela,text="version001",font=("Arial",8),fg="black")
texto.pack()
texto.place(x=240,y=130)

botao = Button(janela,text="Produção Taciclezia",bd=3,command=taciclezia)
botao.pack()
botao.place(x=9,y=15)

botao2 = Button(janela,text="Entrar usuário",bd=3,command=enteruser)
botao2.pack()
botao2.place(x=9,y=53)

botao5 = Button(janela,text="Produção Dr.João",bd=3)
botao5.pack()
botao5.place(x=180,y=15)

janela.mainloop()