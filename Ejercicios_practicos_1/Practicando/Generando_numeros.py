#importamos la librería ramdom

import random

lista_numeros = []
numero_mayor = 0
    
#creamos una funcion que generea numeros aleatorios y encuentra el mayor y el menor
def llenar_lista():
    
    for item in range(0,10):
        numero_aleatorio = random.randint(1,300)
        lista_numeros.append(numero_aleatorio)   
               
    print(lista_numeros) 
    return lista_numeros


def encontrar_mayor(lista: list):        
    max = lista[0]
    for x in lista:
        if x >= max:
            max = x
    
    lista.clear()
    
    return max


def encontrar_menor(lista: list):        
    max = lista[0]
    for x in lista:
        if x <= max:
            max = x
    
    lista.clear()
    
    return max

# print(encontrar_mayor(llenar_lista()))
# print(encontrar_menor(llenar_lista()))
# llenar_lista()