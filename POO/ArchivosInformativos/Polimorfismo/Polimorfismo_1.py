#Polimorfimos

class Animal:
    def sonido(self):
        pass
    
class Gato(Animal):
    def sonido(self):
        return "Miau"


class Perro(Animal):
    def sonido(self):
        return "Guau"
    

obj_gato = Gato()
obj_perro = Perro()

print(obj_gato.sonido())
print(obj_perro.sonido())
