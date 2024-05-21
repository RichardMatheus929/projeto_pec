from tkinter import *
from tkinter import ttk

janela = Tk()

janela.title("PEC_version001")
janela.geometry("300x150+100+200")


texto = Label(janela,text="version001",font=("Arial",8),fg="black")
texto.pack()
texto.place(x=240,y=130)

botao = Button(janela,text="Entrar no site",bd=3)
botao.pack()
botao.place(x=9,y=15)

botao2 = Button(janela,text="Fazer atendimento tardio",bd=3)
botao2.pack()
botao2.place(x=9,y=53)

botao3 = Button(janela,text="Add paciente",bd=3)
botao3.pack()
botao3.place(x=205,y=15)

botao4 = Button(janela,text="Fazer atendimento",bd=3)
botao4.pack()
botao4.place(x=180,y=53)

botao5 = Button(janela,text="Add paciente tardio",bd=3)
botao5.pack()
botao5.place(x=180,y=98)

janela.mainloop()