from tkinter import *
from functions import mensaje

inicio= Tk()

inicio.title("Veterinaria")
inicio.iconbitmap("images\window-icon.ico")
inicio.geometry("950x650")
#root.config(bg="black")

lbl = Label(inicio, text='Este es un label')
lbl.pack()

btn = Button(inicio, text='Mensaje', command=mensaje)
btn.config(fg="black", bg="white")
btn.pack()

inicio.mainloop()

