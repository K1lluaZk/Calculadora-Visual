from tkinter import *

root = Tk()
root.title("Calculadora")
root.iconbitmap("calculadora.ico")

texto1 = Entry(root, font = ("Calibri 20"))
texto1.grid(row = 0, column = 0, columnspan= 4, padx = 5, pady = 5)

i = 0

def click_button(valor):
    global i
    texto1.insert(i, valor, )
    i += 1
    
def borrar():
    texto1.delete(0, END)
    i = 0

def operaciones():
   ecuacion = texto1.get()
   resultado = eval(ecuacion)
   texto1.delete(0, END)
   texto1.insert(0,resultado)
   i = 0

button1 = Button(root, text = "1", width = 5, height = 2, command = lambda: click_button(1))
button1.grid(row = 4, column = 0,  padx = 5, pady = 5 )

button2 = Button(root, text = "2", width = 5, height = 2, command = lambda: click_button(2))
button2.grid(row = 4, column = 1,  padx = 5, pady = 5)

button3 = Button(root, text = "3", width = 5, height = 2, command = lambda: click_button(3))
button3.grid(row = 4, column = 2,  padx = 5, pady = 5)

button_rest = Button(root, text = "-", width = 5, height = 2, command = lambda: click_button("-"))
button_rest.grid(row = 4, column = 3,  padx = 5, pady = 5)



button4 = Button(root, text = "4", width = 5, height = 2, command = lambda: click_button(4))
button4.grid(row = 3, column = 0,  padx = 5, pady = 5)

button5 = Button(root, text = "5", width = 5, height = 2, command = lambda: click_button(5))
button5.grid(row = 3, column = 1,  padx = 5, pady = 5)

button6 = Button(root, text = "6", width = 5, height = 2, command = lambda: click_button(6))
button6.grid(row = 3, column = 2,  padx = 5, pady = 5)

button_sum = Button(root, text = "+", width = 5, height = 2, command = lambda: click_button("+"))
button_sum.grid(row = 3, column = 3,  padx = 5, pady = 5)


button7 = Button(root, text = "7", width = 5, height = 2, command = lambda: click_button(7))
button7.grid(row = 2, column = 0,  padx = 5, pady = 5)

button8 = Button(root, text = "8", width = 5, height = 2, command = lambda: click_button(8))
button8.grid(row = 2, column = 1,  padx = 5, pady = 5)

button9 = Button(root, text = "9", width = 5, height = 2, command = lambda: click_button(9))
button9.grid(row = 2, column = 2,  padx = 5, pady = 5)

button_mult = Button(root, text = "x", width = 5, height = 2, command = lambda: click_button("*"))
button_mult.grid(row = 2, column = 3,  padx = 5, pady = 5)


buttondelete = Button(root, text = "AC", width = 5, height = 2, command = lambda: borrar())
buttondelete.grid(row = 1, column = 0, padx = 5, pady = 5)

buttonparentesis1 = Button(root, text = "(", width = 5, height = 2, command = lambda: click_button("("))
buttonparentesis1.grid(row = 1, column = 1,  padx = 5, pady = 5)

buttonparentesis2 = Button(root, text = ")", width = 5, height = 2, command = lambda: click_button(")"))
buttonparentesis2.grid(row = 1, column = 2,  padx = 5, pady = 5)

button_div = Button(root, text = "÷", width = 5, height = 2, command = lambda: click_button("/"))
button_div.grid(row = 1, column = 3, padx = 5, pady = 5)


button0 = Button(root, text = "0", width = 15, height = 2, command = lambda: click_button(0))
button0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)

button_punto = Button(root, text = ".", width = 5, height = 2, command = lambda: click_button("."))
button_punto.grid(row = 5, column = 2,  padx = 5, pady = 5)

button_igual = Button(root, text = "=", width = 5, height = 2, command = lambda: operaciones())
button_igual.grid(row = 5, column = 3, padx = 5, pady = 5)


root.mainloop()