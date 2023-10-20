#imaginate que estás modelando animales en un zoologico. Crear tres clases: Animal, Mamifero y Ave. La clase Animal debe tener un método llamado comer.
#la clase mamifero debe tener en método llamado amamantar y la clase ave un metood llamado volar

#ahora, crea una clase Murcielago que herede de mamifero y ave, en ese orden y por lo tanto debe ser capaz de amamantar y volar ademas de comer
#finalmente, juega con el orden de herencia de la clase murcielago y observa como acambia el MRO y el comportamiento de los métodos al usar Super()

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer(self):
        return 'estoy comiendo'
    
class Mamifero(Animal):
    def __init__(self):
        pass
    
    def amamantar(self):
        return 'estoy amamantando'

class Ave(Animal):
    def __init__(self):
        pass
    
    def volar(self):
        return 'estoy volando'
    

class murcielago(Mamifero, Ave):
    def __init__(self):
        pass


obj_1 = murcielago()

print(obj_1.amamantar())
print(obj_1.volar())
print(obj_1.comer())