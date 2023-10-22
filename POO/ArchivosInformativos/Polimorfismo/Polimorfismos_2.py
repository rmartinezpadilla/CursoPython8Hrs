# polimorfismo.py
#
# Copyright 2020 <<Pyro>>
class Marino(): #Clase Padre
    def hablar(self): #Método Hablar
        print ("Hola..")
class Pulpo(Marino): #Clase Hija
    def hablar (self): #Método Hablar
        print ("Soy un Pulpo")
class Foca(Marino): #Clase Hija
    def hablar (self, mensaje): #Método Hablar
        print (mensaje)
Pulpito = Pulpo() #Instancia
Foca = Foca() #Instancia
Pulpito.hablar() #Llamamos al método
Foca.hablar("Soy una foca, este es mi mensaje") #Llamamos al método