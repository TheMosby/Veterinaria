from tkinter import *
from tkinter import messagebox


def mensaje():
    messagebox.showinfo("Título del mensaje", "Este es un mensaje de ejemplo.")

def suma(n1 , n2, lbl_resultado):
    num1= float(n1.get())
    num2= float(n2.get())
    resultado= float(num1) + float(num2)
    lbl_resultado.config(text=f"La suma es: {resultado}")

    
    
    