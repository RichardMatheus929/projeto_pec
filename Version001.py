# Tetando criar uma interface agradável com tkinter  -- Ferramentas : Proxlight, tkinter, selenium, Figma -- 
from tkinter import *
from tkinter import ttk
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui as pg

# /html/body/div[1]/div/div[3]/main/div[1]/div/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div/div

def criarxpath(palavra):
    word = palavra
    xpath = f"//*[contains(text(), '{word}')]"
    return xpath
    
def openpag():
    url = "https://esustouros.com.br/"
    navegador.get(url)

def enteruser():

    openpag()

    pg.sleep(4)

    usuario = navegador.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div/div[2]/div[1]/form/div/div[1]/div/div[1]/div/div/input")
    usuario.send_keys('10837388449')

    senha = navegador.find_element(By.NAME,"password")
    senha.send_keys("bolsonaro2024")

    botao = navegador.find_element(By.CLASS_NAME,"css-1mc6ylg")
    botao.click()

    elementoA = WebDriverWait(navegador,4).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1jy51ie")))
    elementoA.click()

    elementoB = WebDriverWait(navegador,4).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1xc5sgu")))
    elementoB.click()

def addpaciente():
    profissional = navegador.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[1]/div/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/div/div/input")
    profissional.send_keys('joao')
    pg.sleep(0.8)
    elementojoao = navegador.find_element(By.ID,profissional.get_attribute("id").replace("input","item")+"-0")
    elementojoao.click()
    pg.sleep(0.25)
    odonto = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div[7]/label')
    odonto.click()
    adicionar = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/div/div[3]/div/div[2]/div/div[2]/div/div[3]/div/button[2]')
    adicionar.click()

def atendimento(n = "5"):
    try:
        
        # bloco exame dentario
        elementoexame = navegador.find_element(By.XPATH,f'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/input')
        elementoexame.send_keys('z012')
        pg.sleep(0.5)
        elementoz012 = navegador.find_element(By.ID,elementoexame.get_attribute("id").replace("input","item")+"-2")
        elementoz012.click()

        # bloco adicionar(botao azul)
        elementoadicionarz012 = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/button')
        elementoadicionarz012.click()

        # bloco não identificado e protese
        elementonaoident = navegador.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div[7]/label")
        elementoprotese = navegador.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[4]/div/div/div/div/div/div/div[2]/div/div[2]/label/span[1]")
        elementonaoident.click()
        elementoprotese.click()

        # bloco orientacao 
        elementoinputorientacao = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/input')
        elementoinputorientacao.send_keys("orientacao de higiene")
        pg.sleep(0.8)
        elementoorientacao = navegador.find_element(By.ID,elementoinputorientacao.get_attribute('id').replace("input","item")+"-0")
        elementoorientacao.click()

        # bloco primeira consulta e atendimento compartilhado
        elemento1consulta = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[6]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/span[1]/div/label')
        elemento1consulta.click()
        elementocompartilhado = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[6]/div[2]/div/div/div[3]/div/div/div/div/div/div/input')
        elementocompartilhado.send_keys('taciclezia')
        pg.sleep(0.8)
        elementotaciclezia = navegador.find_element(By.ID,elementocompartilhado.get_attribute('id').replace("input","item")+"-0")
        elementotaciclezia.click()
        elementoretorno = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[6]/div[2]/div/div/div[8]/div/div/div/div/div[2]/div/div[2]/div[1]/label')
        elementoretorno.click()
        pg.sleep(0.25)
        elementovolta = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[5]/div[2]/div/div/div[3]/div/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/label[1]')
        elementovolta.click()
        elementofinal = navegador.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/main/div[1]/form/div[2]/div/div/div/div[2]/button[2]')
        elementofinal.click()

    except TimeoutException:
        print("Lasco")
    except NoSuchElementException:
        print("Não lascou tanto pelo menos")

def atendimentotardio(n = "5"):
    try:

        elementoatendimento = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div[2]/button[1]')
        elementoatendimento = navegador.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/main/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/button[1]')
        elementoatendimento.click()
        pg.sleep(1)
        elementosoap = navegador.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/main/header/div/div/div[2]/ul/li[2]/a')
        elementosoap.click()
        pg.sleep(1)        
        # bloco exame dentario
        elementoexame = navegador.find_element(By.XPATH,f'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/input')
        elementoexame.send_keys('z012')
        pg.sleep(0.5)
        elementoz012 = navegador.find_element(By.ID,elementoexame.get_attribute("id").replace("input","item")+"-2")
        elementoz012.click()

        # bloco adicionar(botao azul)
        elementoadicionarz012 = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/button')
        elementoadicionarz012.click()

        # bloco não identificado e protese
        elementonaoident = navegador.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div[7]/label")
        elementoprotese = navegador.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[2]/div/div/div/div/div[4]/div/div/div/div/div/div/div[2]/div/div[2]/label/span[1]")
        elementonaoident.click()
        elementoprotese.click()

        # bloco orientacao 
        elementoinputorientacao = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/input')
        elementoinputorientacao.send_keys("orientacao de higiene")
        pg.sleep(0.8)
        elementoorientacao = navegador.find_element(By.ID,elementoinputorientacao.get_attribute('id').replace("input","item")+"-0")
        elementoorientacao.click()

        # bloco primeira consulta e atendimento compartilhado
        elemento1consulta = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[6]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/span[1]/div/label')
        elemento1consulta.click()
        elementocompartilhado = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[6]/div[2]/div/div/div[3]/div/div/div/div/div/div/input')
        elementocompartilhado.send_keys('taciclezia')
        pg.sleep(0.8)
        elementotaciclezia = navegador.find_element(By.ID,elementocompartilhado.get_attribute('id').replace("input","item")+"-0")
        elementotaciclezia.click()
        elementoretorno = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[6]/div[2]/div/div/div[8]/div/div/div/div/div[2]/div/div[2]/div[1]/label')
        elementoretorno.click()
        pg.sleep(0.25)
        elementovolta = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/main/div[1]/form/div[1]/div/div/div[2]/div/div/div[5]/div[2]/div/div/div[3]/div/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div/label[1]')
        elementovolta.click()
        elementofinal = navegador.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/main/div[1]/form/div[2]/div/div/div/div[2]/button[2]')
        elementofinal.click()

        pg.sleep(1)
        atendimentotardio()

    except TimeoutException:
        print("Lasco")
    except NoSuchElementException:
        print("Não lascou tanto pelo menos")

def atalho(event):
    addpaciente("1")

def addpacientetardio():
    localatendimento = navegador.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/main/div[1]/div/div[3]/div/div[3]/div/div[2]/div/div[5]/div/div[1]/div/div/div/div/input").get_attribute("id")
    ubs = navegador.find_element(By.ID,localatendimento)
    ubs.click()


# hora = "0"
# contador = 0
# def hora():
#     horario = "08:00"    
    

# ---- Interface gráfica a partir daqui ----
        
janela = Tk()
janela.bind("<Control-a>", atalho)
janela.title("PEC_version001")
janela.geometry("300x150+100+200")

navegador = Chrome()

texto = Label(janela,text="version001",font=("Arial",8),fg="black")
texto.pack()
texto.place(x=240,y=130)

botao = Button(janela,text="Entrar no site",bd=3,command=openpag)
botao.pack()
botao.place(x=9,y=15)

botao2 = Button(janela,text="Entrar usuário",bd=3,command=enteruser)
botao2.pack()
botao2.place(x=9,y=53)

botao3 = Button(janela,text="Add paciente",bd=3,command=addpaciente)
botao3.pack()
botao3.place(x=9,y=98)

botao5 = Button(janela,text="Add paciente tardio",bd=3)
botao5.pack()
botao5.place(x=180,y=15)

botao4 = Button(janela,text="Fazer atendimento",bd=3,command=atendimento)
botao4.pack()
botao4.place(x=180,y=53)

botao6 = Button(janela,text="Fazer atendimento tardio",bd=3,command=atendimentotardio)
botao6.pack()
botao6.place(x=150,y=98)

janela.mainloop()
