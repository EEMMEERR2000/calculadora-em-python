# importando tkinter
from tkinter import *
from tkinter import ttk

cor1 = "#1e1f1e"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"
 
janela = Tk()
janela.title("calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

Frame_tela = Frame(janela, width=235, height=50, bg=cor3)
Frame_tela.grid(row=0, column=0)

Frame_C = Frame(janela, width=235, height=268)
Frame_C.grid(row=1, column=0)

valor_texto = StringVar
resultado = IntVar
todos_valores = ''

valor_texto = StringVar()

def entrar_valor(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores) # type: ignore

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

app_label = Label(Frame_tela,textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT,font=('Ivy 18'),bg=cor3,fg=cor2)
app_label.place(x=0, y=0)

b_1 = Button(Frame_C,command=limpar_tela, text="C", width=11, height=2,bg=cor4, font=( 'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(Frame_C,command= lambda: entrar_valor('%'), text="%", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(Frame_C, text="/", width=5, height=2,bg=cor5,fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(Frame_C, command= lambda: entrar_valor('7'),text="7", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_4 = Button(Frame_C,command= lambda: entrar_valor('8'), text="8", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=59, y=52)
b_4 = Button(Frame_C, command= lambda: entrar_valor('9'),text="9", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=118, y=52)
b_3 = Button(Frame_C,command= lambda: entrar_valor('*'), text="*", width=5, height=2,bg=cor5,fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=52)

b_5 = Button(Frame_C,command= lambda: entrar_valor('4'), text="4", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=0, y=104)
b_5 = Button(Frame_C,command= lambda: entrar_valor('5'), text="5", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=104)
b_5 = Button(Frame_C,command= lambda: entrar_valor('6'), text="6", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=118, y=104)
b_5 = Button(Frame_C, command= lambda: entrar_valor('-'),text="-", width=5, height=2,bg=cor5,fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=177, y=104)

b_6 = Button(Frame_C,command= lambda: entrar_valor('1'), text="1", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=0, y=156)
b_6 = Button(Frame_C, command= lambda: entrar_valor('2'),text="2", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=59, y=156)
b_6 = Button(Frame_C, command= lambda: entrar_valor('3'),text="3", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=156)
b_6 = Button(Frame_C,command= lambda: entrar_valor('+'), text="+", width=5, height=2,bg=cor5,fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=177, y=156)

b_7 = Button(Frame_C, command= lambda: entrar_valor('0'),text="0", width=11, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=208)
b_7 = Button(Frame_C,command= lambda: entrar_valor('.'), text=".", width=5, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=118, y=208)
b_7 = Button(Frame_C, command= calcular,text="=", width=5, height=2,bg=cor5,fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=208)

janela.mainloop()