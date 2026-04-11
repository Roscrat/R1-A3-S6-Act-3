from tkinter import *

root = Tk()

def mensaje():
    Label(root, text="No vuelvas a presionar").grid(row=1)

boton = Button(root, text="Presiona", command=mensaje)
boton.grid(row=0)

root.mainloop()