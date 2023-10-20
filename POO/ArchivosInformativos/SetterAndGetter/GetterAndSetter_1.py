#aplicando método getter  and setter para acceder a las propiedades de una clase desde dentro o desde afuer de ella misma
#la forma convencional
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        self._edad = edad
        
obj = Persona("Juan", 23)
print(obj._nombre)
print(obj._edad)

obj.set_nombre("Luis")
obj.set_edad(26)


print(obj.get_nombre(), obj.get_edad())

