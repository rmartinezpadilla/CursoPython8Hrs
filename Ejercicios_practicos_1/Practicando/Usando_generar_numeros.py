from Generando_numeros import *

cantidad = input('Dame la cantidad de veces que quieres realizar la operacion: ')
cantidad1 = int(cantidad)
iteraciones = 0

while cantidad1 >= iteraciones:  
  print(encontrar_mayor(llenar_lista()))
  print(encontrar_menor(llenar_lista()))
  iteraciones +=1