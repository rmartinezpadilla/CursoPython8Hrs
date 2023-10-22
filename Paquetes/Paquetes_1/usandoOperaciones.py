#este est  para las operaciones que estan en el arcchivo "opraciones"
#from calculos.operaciones import * 

#este es para las operaciones ya separadaras cada una en sus paquetes
from calculos.basicos.operaciones_basicas import *

#es decir solo vamos a llamar los metodos que existen en este modulo
print(suma(3,9))

print(multi(36,5))
#redondear no existe por eso lo comentamos
#print(redondear(9.661))

#si quisieramos usar la función redondear tocaría llamar el modulo usando la ruta del paquete de donde se encuenta esta funcion
