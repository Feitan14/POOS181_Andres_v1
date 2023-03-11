from tkinter import Tk,Frame,Button,messagebox
import random
import string
#4funcion boton 
def mostrarMensaje():
    messagebox.showinfo("","")
    
#5. Funcion para agregar botones
def agregarBoton():
    botonAzul.config(text="+", bg="green",fg="black")
    botonNuevo = Button(seccion1, text="Boton Nuevo")
    botonNuevo.pack()

#instanciamos el objeto ventana
ventana = Tk()
ventana.title("practica 13: contraseña")
ventana.geometry("600x400")

#2. Definimos secciones de la ventana
seccion1=Frame(ventana)
seccion1.pack(expand=True,fill='both')

#3. Botones
botonAzul=Button(seccion1,text="Aceptar",fg="black",command=mostrarMensaje)
botonAzul.place(x=60, y=60)

#generador
def generate_password(length=8, include_uppercase=False, include_special=False):
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_special:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_password_strength(password):
    """
    Checks the strength of a password and returns a string describing its strength.
    """
    # This is just a simple example of how to check password strength. A more comprehensive check could be implemented if desired.
    if len(password) < 8:
        return "Fácil"
    elif len(password) < 12:
        return "Medio"
    else:
        return "Buena"
