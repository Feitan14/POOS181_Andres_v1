from tkinter import messagebox,Label
from ventana_12 import*
import tkinter as tk

def mostrarMensaje():
    messagebox.showinfo("","")
a = ventana_12()

def ejecutar():
    a.validar(var1.get()var2.get())
    

def main():
    
    messagebox.showinfo("Ingresa la longitud de la contraseña (minimo 8 caracteres): ")
    password = passN_entry.get()
    if length == '':
        length = 8
    else:
        length = int(length)
    include_uppercase = Label(seccion1, text="Incluir letras mayúsculas? (s/n): ").lower() == 's'
    include_special = Entry("Inlcuira caracteres especiales? (s/n): ").lower() == 's'
    
    # Generar la contraseña
    var1 =tk.StringVar()
    passN_entry = generate_password(length, include_uppercase, include_special)
    strength = check_password_strength(password)
    #imprimimos los valores
    var2= tk.StringVar()
    textcontra= Label(seccion1,text="Contraseña generada:", password).pack()
    textcontra= Label("Seguridad de la contraseña:", strength).pack()
    
#main de ejecucion de la ventana
ventana.mainloop()