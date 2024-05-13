from tkinter import *
from tkinter import ttk

cor_roxa= "#2b0f3d"
cor_branca= "#fcfcfc"
cor_laranja="#fa7a0a"
cor_verde="#0afa0a"
cor_azul= "#020bb8"
cor_cinza="#a9abaa"


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config()

#criando frames

frame_tela = Frame(janela, width=235, height=50, bg=cor_roxa)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=270)
frame_corpo.grid(row=1,column=0) 

#Variáveis

todos_valores=''

#Criando Label
valor_texto = StringVar()

#Funções

def entrar_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)
    

    #passando o valor para a tela
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

def limpar_tela():

    global todos_valores
    todos_valores = ""
    valor_texto.set("")




#Criando Label

app_label = Label(frame_tela, textvariable=valor_texto, width=15, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 bold'),bg=cor_roxa, fg=cor_branca)
app_label.place(x=0,y=0)

#Primeira linha botões

b_1 = Button(frame_corpo, command= limpar_tela, text="C", width=11, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command= lambda: entrar_valores('%') ,text="%", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)

b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)   
b_3.place(x=180, y=0)


#Segunda linha botões

b_21 = Button(frame_corpo, command= lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_21.place(x=0, y=52)

b_22 = Button(frame_corpo, command= lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_22.place(x=60, y=52)

b_23 = Button(frame_corpo, command= lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)   
b_23.place(x=120, y=52)

b_24 = Button(frame_corpo, command= lambda: entrar_valores('*'), text= "*", width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_24.place(x=180, y=52)

#Terceira linha boões

b_31 = Button(frame_corpo, command= lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_31.place(x=0, y=104)

b_32 = Button(frame_corpo, command= lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_32.place(x=60, y=104)

b_33 = Button(frame_corpo, command= lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)   
b_33.place(x=120, y=104)

b_34 = Button(frame_corpo, command= lambda: entrar_valores('-'), text= "-", width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_34.place(x=180, y=104)

#Quarta linha boões

b_41 = Button(frame_corpo, command= lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_41.place(x=0, y=156)

b_42 = Button(frame_corpo, command= lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_42.place(x=60, y=156)

b_43 = Button(frame_corpo, command= lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)   
b_43.place(x=120, y=156)

b_44 = Button(frame_corpo, command= lambda: entrar_valores('+'), text= "+", width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_44.place(x=180, y=156)

#Quinta linha botôes

b_51 = Button(frame_corpo,command= lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_51.place(x=0, y=208)

b_52 = Button(frame_corpo,command= lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor_cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_52.place(x=120, y=208)

b_52 = Button(frame_corpo, text="=", command= calcular, width=5, height=2, bg=cor_laranja, fg=cor_branca, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_52.place(x=180, y=208)

#Funções



janela.mainloop()

