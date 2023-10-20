#importamos la clase persona para poder usar sus metodos y atributos
#import Persona
from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion, gastos):        
        #llamamos al metodo super para acceder a la clase padre
        super().__init__(nombre, edad, profesion)       
        self.__gastos = gastos             
        
    @property
    def gastos(self):
        return self.__gastos
    
    @gastos.setter
    def gastos(self, valor):
        self.__gastos=valor
        
    
est_1 = Estudiante("Juan", 23, "Alfarero", 3.651)

print(est_1.datos_completos())
print('mis gatos son: ' , str(est_1.gastos))