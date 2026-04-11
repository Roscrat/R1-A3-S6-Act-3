from tkinter import *

root = Tk()

entrada = Entry(root)
entrada.grid(row=0)

def enviar():
    Label(root, text=entrada.get()).grid(row=2)

boton = Button(root, text="Enviar", command=enviar)
boton.grid(row=1)

root.mainloop()