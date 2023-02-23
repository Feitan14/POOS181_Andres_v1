#1. importar clase
from personaje import*
#2.Solicitar atributos para el objeto
print("")
print("### solicitud de datos del heroe ###")
esph = input("Escribe la especie del heroe: ")
nomh = input("Escribe el nombre del heroe: ")
alth = float(input("Escribe la altura del heroe: "))
cargah = int(input("Cuantas balas se recargaran: "))

print("")
print("### solicitud de datos del villano ###")
espv = input("Escribe la especie del villano: ")
nomv = input("Escribe el nombre del vilano: ")
altv = float(input("Escribe la altura del villano: "))
cargav = int(input("Cuantas balas se villano: "))

#3. creamos 2 objetos
heroe=Personaje(esph,nomh,alth)
villano=Personaje(espv,nomv,altv)

#4. acceder a sus atributos y metodos de cada objeto
print("")
print("el personaje pertenece a el grupo mercenario: " + heroe.especie)
print("el personaje se llama: " + heroe.nombre)
print("el personaje mide: " + str(heroe.altura) + "metros")

heroe.correr(True)
heroe.lanzarGranada()
heroe.recargararma(cargah)

print("ATRIBUTOS PERSONAJES")
print("el personaje pertenece a la raza: " + villano.especie)
print("el personaje se llama: " + villano.nombre)
print("el personaje mide: " + str(villano.altura) + "metros")

villano.correr(False)
villano.lanzarGranada()
villano.recargararma(cargav)