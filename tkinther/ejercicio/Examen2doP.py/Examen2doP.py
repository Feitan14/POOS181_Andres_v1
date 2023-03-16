import tkinter as tk
from tkinter import Button, messagebox
import random

# Función para generar la matrícula
# #agregamos los mensajes a pantalla
def generar_matricula():
    nombre = nombre_entry.get()
    apellido_paterno = ap_entry.get()
    apellido_materno = am_entry.get()
    fecha_nacimiento = fn_entry.get()
    a_curso = ac_entry.get()
    carrera = ca_entry.get()
    
    #matricula = + nombre[:1] + apellido_paterno[:2] + apellido_materno[:2] + fecha_nacimiento[-2:] + a_curso[:-2] + carrera[:3] 
   
    matricula = nombre[:1] + apellido_paterno[:2] + apellido_materno[:2] + fecha_nacimiento[-2:] +a_curso[-2:] + carrera[:3]

    # aqui agregaremos 2 numeros random en la matricula
    matricula += str(random.randint(0, 9)) + str(random.randint(0, 9)) 
    matricula_label.config(text="Tu matrícula es: " + matricula)

#impresion de boton
def mostrarm():
    messagebox.showinfo('tu matricula es')
# Creación de la ventana
ventana = tk.Tk()
ventana.title("Generador de Matrícula")
ventana.geometry("600x400")

# Creación de los widgets
nombre_label = tk.Label(ventana, text="Nombre: ")
nombre_entry = tk.Entry(ventana)

ap_label = tk.Label(ventana, text="Apellido Paterno: ")
ap_entry = tk.Entry(ventana)

am_label = tk.Label(ventana, text="Apellido Materno: ")
am_entry = tk.Entry(ventana)

fn_label = tk.Label(ventana, text="Fecha de Nacimiento, ingresa con (DD/MM/AAAA): ")
fn_entry = tk.Entry(ventana)

ca_label = tk.Label(ventana, text="Carrera: ")
ca_entry = tk.Entry(ventana)

ac_label = tk.Label(ventana, text='Año en curso: ')
ac_entry = tk.Entry(ventana)

generar_button = tk.Button(ventana, text="Generar Matrícula", command=generar_matricula)

matricula_label = tk.Label(ventana, text="Tu matrícula aparecerá aquí" )

# empezamos a realizar las posiciones de los widgets
nombre_label.grid(row=0, column=0)
nombre_entry.grid(row=0, column=1)

ap_label.grid(row=1, column=0)
ap_entry.grid(row=1, column=1)

am_label.grid(row=2, column=0)
am_entry.grid(row=2, column=1)

fn_label.grid(row=3, column=0)
fn_entry.grid(row=3, column=1)

ca_label.grid(row=4, column=0)
ca_entry.grid(row=4, column=1)

ac_label.grid(row=5, column=0)
ac_entry.grid(row=5, column=1)

#Generamos un boton para generar la matricula
generar_button.grid(row=6, column=1)

matricula_label.grid(row=6, column=0, columnspan=2)
#imprimimos la matricula y la posicionamos
#main de ejecucion de la ventana
ventana.mainloop()
