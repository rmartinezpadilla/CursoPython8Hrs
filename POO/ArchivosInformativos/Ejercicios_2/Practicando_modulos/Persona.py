#aqui voy a usar la abstraccion para obligar a la clase que herede de esta que implemente estos datos
#ademas las propiedades son privadas
from abc import ABC, abstractclassmethod

class Persona(ABC):
    #obligamos a la clase que herede esta a utilizar estos metodos
    @abstractclassmethod
    def __init__(self, nombre, edad, profesion):
        self.__nombre = nombre
        self.__edad = edad
        self.__profesion = profesion
    
    #@abstractclassmethod
    def datos_completos(self):        
        return f'Mi nombre es {self.__nombre}, tengo {self.__edad} de edad, y soy {self.__profesion}'
    