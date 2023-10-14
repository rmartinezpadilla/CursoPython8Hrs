#Escribir una función que reciba una muestra de números 
# en una lista y devuelva su media.

def dameMediaDeNumeros(listaNumeros):
    media = sum(listaNumeros) / len(listaNumeros)
    return media

print(dameMediaDeNumeros([2, 54, 23, 62, 41, 900]))


numero = int(input("dame el número: "))

print('el tio de dato es')
print(type(numero))
print(f' el número es: {numero}')
