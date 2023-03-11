import tkinter as tk
from logica_ve import *

class Ventana(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Practica 13: Contraseña automatica")
        self.geometry("600x400")
        self.lenlabel = tk.Label(text="Longitud de la contraseña:")
        self.lenlabel.pack()
        self.entryLen = tk.Entry(self)
        self.entryLen.pack()
        self.estado = tk.BooleanVar()
        
        self.estado1 = tk.BooleanVar()
        self.checkboxm = tk.Checkbutton(self, text="Desea incluir mayusculas",variable=self.estado,onvalue=True, offvalue=False)
        self.checkboxm.pack()
        self.checkboxes = tk.Checkbutton(self, text="Desea incluir caracteres especiales",variable=self.estado1,onvalue=True, offvalue=False)
        self.checkboxes.pack()
        self.button = tk.Button(self, text="Generar Contraseña", command=self.on_button)
        self.button.pack()
        
    def on_button(self):
        seg=aaa(self.entryLen.get(),self.estado.get(),self.estado1.get())
        seg.checarSeguridad(int(self.entryLen.get()))
        gen=aaa(self.entryLen.get(),self.estado.get(),self.estado1.get())
        gen.generarContraseña(int(self.entryLen.get()),self.estado.get(),self.estado1.get())
        print(self.entryLen.get())
        print(self.estado.get())
        print(self.estado1.get())

ventana = Ventana()
ventana.mainloop()