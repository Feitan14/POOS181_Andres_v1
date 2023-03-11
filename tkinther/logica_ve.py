from tkinter import messagebox
import random
import string

class aaa:
    def __init__(self, len,mayus,espe):
        self.__longitud=len
        self.__checkmayus=mayus
        self.__checkspe=espe


    def checarSeguridad(self,parametro):
        
        if parametro  < 8:
            messagebox.showinfo("contraseña","La contraseña es debil, es la siguiente")
        elif parametro  < 12:
            messagebox.showinfo("contraseña","La contraseña es normal, es la siguiente")
        elif parametro  >= 13:
            messagebox.showinfo("contraseña","La contraseña es buena, es la siguiente")   
                
    def generarContraseña(self,long, include_uppercase=False, include_special=False):
        chars = string.ascii_lowercase
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_special:
            chars += string.punctuation
        password = ''.join(random.choice(chars) for _ in range(long))
        messagebox.showinfo("la contraseña es: ",password)
