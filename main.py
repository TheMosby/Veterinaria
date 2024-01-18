from tkinter import *
from functions import suma

inicio= Tk()

inicio.title("Veterinaria")
inicio.iconbitmap("images\window-icon.ico")
mycolor = '#E0E0E0'  # or use hex if you prefer 
inicio.geometry("900x450")
#root.config(bg="black")

lbl_1 = Label(inicio, text='Primer numero')
lbl_1.place(x=10, y=10, width=100, height=30)

txt_1 = Entry(inicio, bg=mycolor)
txt_1.place(x=150, y=10, width=100, height=30)

lbl_2 = Label(inicio, text='Segundo numero')
lbl_2.place(x=10, y=50, width=100, height=30)

txt_2 = Entry(inicio, bg=mycolor)
txt_2.place(x=150, y=50, width=100, height=30)

lbl_3 = Label(inicio, text="resultado")
lbl_3.place(x=95, y=90, width=100, height=30)

btn = Button(inicio, text='Mensaje', command=lambda: suma(txt_1, txt_2, lbl_3))
btn.place(x=270, y=25, width=100, height=30)
#btn.config(fg="blue", bg="white")
btn["fg"]="white"
btn["bg"]="black"


inicio.mainloop()

