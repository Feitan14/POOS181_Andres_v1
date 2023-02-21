class Personaje:
    
    #atributos del personaje
    especie = "Genei Ryodan"
    nombre = "Feitan Portor"
    altura = 1.60
    
    #metodos personaje
    def correr(self,status):
        if(status):
            print("el personaje "+ self.nombre + " esta corriendo")
            else:  print("el personaje "+ self.nombre + " se detuvo")
    def lanzarGranada(self):
        print("se lanzo granada ")
        def recargararma(self,municiones):
            cargador = 5
            cargador = cargador + municiones
            print("el arma tiene ahora " +cargador+ " balas")