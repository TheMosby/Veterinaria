from tkinter import *


def abrir_ventana():
    
    # Crear una nueva ventana
    nueva_ventana = Tk()

     # Agregar widgets a la nueva ventana
    etiqueta = Label(nueva_ventana, text="¡Nueva ventana!")
    etiqueta.pack(padx=20, pady=20)

    boton_cerrar = Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
   
    boton_cerrar.pack(pady=10)