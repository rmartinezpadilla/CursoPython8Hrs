#vamsoa  declarar setter y getter usando decoradores
#aplicando método getter  and setter para acceder a las propiedades de una clase desde dentro o desde afuer de ella misma
#USANDO DECORADORES *********IMPORTANTE*******
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    #*********IMPORTANTE*******
    #Algo a tener en cuenta para crear los metodos getter y setter en python es que ambos deben tener el mismo nombre
    #para los getter usamos el decorador @property
    #la diferencia es que al usarlo vamos a llamar al método sin paréntesis
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    #para los getter usamos el decorador @property
    #la diferencia es que al usarlo vamos a llamar al método sin paréntesis
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
        
obj = Persona("Juan", 23)

#aqui usamos el método Get, es decir, el propeties sin parentesis
print(obj.nombre)
#aqui usamos el método Get, es decir, el propeties sin parentesis
print(obj.edad)
#intentamos modificar el valor de la variale --> sale un error por eso se comenta
#obj.get_nombre = "lulo"

#aqui usamos el método Setter simplemente llamamos al método y le damos los nuevos valores, como tiene el decorador
#al tener el decorador va a funcionar como un atributo de esta manera ocultamos el nombre real de la variable
obj.nombre="Mirella"
print(obj.nombre)
#aqui usamos el método Setter, es decir, el propeties sin parentesis
obj.edad = 30
print(obj.edad)
#intentamos modificar el valor de la variale --> sale un error por eso se comenta
#obj.get_nombre = "lulo"


