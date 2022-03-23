from cgitb import text
import os 
from tkinter import *
from tkinter import font



cor1 = '#2a282b' #preto
cor2 = '#502b78' #roxo

janela = Tk()
janela.title("Hora de mimir")
janela.geometry("300x250")
janela.config(bg=cor2)


def meia_hora():
    os.system("shutdown /s /t 1800")

def uma_hora():
    os.system("shutdown /s /t 3600")

def um_hora_meia():
    os.system("shutdown /s /t 5400")

def duas_horas():
    os.system("shutdown /s /t 7200")

def duas_hora_meia():
    os.system("shutdown /s /t 9000")

def tres_horas():
    os.system("shutdown /s /t 10800")

def cancelar():
    os.system("shutdown /a")


#Criar Frames-----------------------------------------------------------
frame_cima =Frame(janela,width=300,height=60,bg=cor2,padx=0,pady=0,relief='flat')
frame_cima.grid(row=0,column=0,sticky=NSEW)

frame_baixo = Frame(janela,width=300,height=210,bg=cor1,relief='flat')
frame_baixo.grid(row=1,column=0,columnspan=3)

#-----------------------------------------------------------
label_cima = Label(frame_cima,text='Hora de dormir\nescolha o tempo de desligamento',width=300 ,height=2,padx=0, relief='flat',anchor='nw',font='Ivy 10 bold',bg=cor2,fg='white')
label_cima.place(x=40,y=10)

#criar botão-------------------------------------

botao1 = Button(frame_baixo,command=meia_hora,width=10,height=2,text='30 min',relief='raised')
botao1.place(x=5,y=5)

botao2 = Button(frame_baixo,command=uma_hora,width=10,height=2,text='1h',relief='raised')
botao2.place(x=105,y=5)

botao3 = Button(frame_baixo,command=um_hora_meia,width=10,height=2,text='1:30h',relief='raised')
botao3.place(x=205,y=5)

botao4 = Button(frame_baixo,command=duas_horas,width=10,height=2,text='2h',relief='raised')
botao4.place(x=5,y=60)

botao5 = Button(frame_baixo,command=duas_hora_meia,width=10,height=2,text='2:30h',relief='raised')
botao5.place(x=105,y=60)

botao6 = Button(frame_baixo,command=tres_horas,width=10,height=2,text='3h',relief='raised')
botao6.place(x=205,y=60)

botao6 = Button(frame_baixo,command=cancelar,width=30,height=2,text='Cancelar',relief='raised')
botao6.place(x=38,y=130)





janela.mainloop()