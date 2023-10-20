#las clases abstractas no se pueden instanciar, obligan a que otra clase hereden de ella
# por lo general se usan como modelo general

#para implementar las clases abstractas debemos importar la siguiente librería
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def a_que_se_dedica(self):
        pass
    
    def presentarse(self):
        return f'Hola, mi nombre es: {self.nombre} y tengo {self.edad} años'

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
      super().__init__(nombre, edad, sexo, actividad)
    
    def a_que_se_dedica(self):
        return f'Actualmente estudio: {self.actividad}'
    
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
      super().__init__(nombre, edad, sexo, actividad)
    
    def a_que_se_dedica(self):
        return f'Actualmente trabajo: {self.actividad}'
      
#mi_persona =Persona("juan", 23, "M", "HTML")

mi_estudiante_a = Estudiante("juan", 23, "M", "HTML")
mi_empleado_a = Trabajador("María", 39, "F", "Secretaria")

print(mi_estudiante_a.presentarse())
print(mi_estudiante_a.a_que_se_dedica())
print(mi_empleado_a.presentarse())
print(mi_empleado_a.a_que_se_dedica())