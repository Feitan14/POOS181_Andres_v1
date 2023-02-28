from tkinter import Tk,Frame,Button

#1. instanaciamos un objeto ventana
ventana = Tk()
ventana.title("practica 11: Frames")
ventana.geometry("600x400")

#2. Definimos secciones de la ventana
seccion1=Frame(ventana,bg="#39FF33")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="#41FFC0")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana,bg="#D8FF27")
seccion3.pack(expand=True,fill='both')

#3. Botones
botonAzul=Button(seccion1,text="boton azul",fg="blue",bg="black")
botonAzul.place(x=60, y=60)

botonAmarillo=Button(seccion2,text="boton amarillo",fg="yellow",bg="black")
botonAmarillo.grid(row=0, column=0)

botonNegro=Button(seccion2,text="boton negro",fg="black")
botonNegro.grid(row=0, column=2)

botonVerde=Button(seccion3,text="boton negro",fg="#27FF52",bg="black")
botonVerde.pack()


#main de ejecucion de la ventana
ventana.mainloop()