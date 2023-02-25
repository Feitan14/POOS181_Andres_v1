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
print("")
#3. creamos 2 objetos

heroe=Personaje(esph,nomh,alth)
villano=Personaje(espv,nomv,altv)

#Ejemplo set, esto hace que afuerzas sea lo que dice el SET
heroe.setnombre("pepe pecas xd")

#4. acceder a sus atributos y metodos de cada objeto

print("")
print("el personaje pertenece a el grupo mercenario: " +heroe.getespecie())
print("el personaje se llama: " + heroe.getnombre())
print("el personaje mide: " + str(heroe.getaltura()) + "metros")
heroe.correr(True)
heroe.lanzarGranada()
heroe.recargararma(cargah)
heroe.__pensar()
print("")

print("")
print("ATRIBUTOS PERSONAJES")
print("el personaje pertenece a la raza: " + villano.getespecie())
print("el personaje se llama: " + villano.getnombre())
print("el personaje mide: " + str(villano.getaltura()) + "metros")
villano.correr(False)
villano.lanzarGranada()
villano.recargararma(cargav)