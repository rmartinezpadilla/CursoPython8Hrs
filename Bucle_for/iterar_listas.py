animales = ["Perro", "gato", "loro", "pescado"]
numeros = [10, 20 ,6, 9]

#recorriendo la lista de animales
for animal in animales:
    print(animal)
    print(f'ahora la variable tiene el valor de: {animal}')
    
#recorriendo la lista de numeros
for numero in numeros:
    resultado = numero * 3
    print(resultado)

#recorriendo ambas listas usando la función zip()
for animal, numero in zip(animales, numeros):
    print(animal)
    print(numero)
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es {valor}')
    

#imprimiendo varios datos y usando else
for valor in range(10):
    print(valor)
else:
    print("acabamos...")

#imprimiendo varios datos
for valor in range(10):
    print(valor)

#imprimiendo varios datos II
for valor_2 in range(10, 15):
    print(valor_2)