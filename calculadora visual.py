import tkinter as tk
from tkinter import messagebox 

def calcular():
    try:
        var1 = float(entry_var1.get())
        var2 = float(entry_var2.get())
        operacion = op.get()
        
        if operacion == 1:
            resultado = var1 + var2
        elif operacion == 2:
            resultado = var1 - var2
        elif operacion == 3:
            resultado = var1 * var2
        elif operacion == 4:
            if var2 != 0:
                resultado = var1 / var2
            else:
                messagebox.showerror("Error", "No se puede dividir entre cero")
                return
        else:
            messagebox.showwarning("Operación inválida", "Selecciona una operación válida")
            return
        
        label3.config(text=f"Resultado: {resultado}")
    except ValueError:
         messagebox.showerror("Error", "Por favor, ingresa números válidos")

root = tk.Tk()
root.title("Calculadora")

entry_var1 = tk.Entry(root)
entry_var2 = tk.Entry(root)

op = tk.IntVar()
op.set(1)

label1 = tk.Label(root, text= "Primer numero:")
label2 = tk.Label(root, text= "Segundo numero:")
label3 = tk.Label(root, text= "Resultado:")

rbutton1 = tk.Radiobutton(root, text="Suma", variable=op, value=1)
rbutton2 = tk.Radiobutton(root, text="Resta", variable=op, value=2)
rbutton3 = tk.Radiobutton(root, text="Multiplicación", variable=op, value=3)
rbutton4 = tk.Radiobutton(root, text="División", variable=op, value=4)

button_calcular = tk.Button(root, text="Calcular", command=calcular)

label1.grid(row=0, column=0)
entry_var1.grid(row=0, column=1)

label2.grid(row=1, column=0)
entry_var2.grid(row=1, column=1)

rbutton1.grid(row=2, column=0)
rbutton2.grid(row=2, column=1)
rbutton3.grid(row=3, column=0)
rbutton4.grid(row=3, column=1)

button_calcular.grid(row=4, column=0, columnspan=1)
label3.grid(row=5, column=0, columnspan=1)

root.mainloop()