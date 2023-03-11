from tkinter import *
from tkinter import Label, PhotoImage
from caja_popular import *

# Crea una nueva ventana
ventana = Tk()

# Configura la ventana
ventana.title("Mi ventana")
ventana.geometry("500x500")

# Carga la imagen
imagen_fondo = PhotoImage(file="C:\Users\andy2\Downloads\eluriboing.jpg")

# Crea una etiqueta para la imagen y la coloca en la ventana
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Ejecuta la ventana
ventana.mainloop()