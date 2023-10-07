#Ejercicio 1
nombre = input("dame tu nombre: ")
print("hola " + nombre + "!")

#Ejercicio 2
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
# por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
inicio = 1
nombre = input("Dame tu nombre: ")
cantidad = input("Dime la cantidad de veces a imprimir el número: ")
inicio+=1
for cantidad in range(inicio, cantidad):
 print(nombre)
 