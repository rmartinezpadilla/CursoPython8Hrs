# se pone el asterisco antes del nombre del parametro para decirle a python
# que en este caso vamos a recibir un número indeterminado de datos
#ademas de eso, los recibe como tuplas
#Yield from es para recorrer dos arreglos, tuplas, filas
#es como un for aniadado

### esta es la forma normal de hacerlo
def generaCiudades(*ciudades):
    for elemento in ciudades:
        for dato in elemento:
            yield dato

ciudades_mostradas = generaCiudades("Montería", "Planeta", "Lorica", "Medellín")        

print(next(ciudades_mostradas))
print("mostrando otra ciudad...")
print(next(ciudades_mostradas))
print("mostrando otra ciudad...")

### esta es la forma mejorada de hacerlo

def generaCiudades(*ciudades):
    for elemento in ciudades:
        #eliminamos el ciclo for anidado y usamos la sentencia yield from
        yield from elemento

ciudades_mostradas = generaCiudades("Montería", "Planeta", "Lorica", "Medellín")        
print(next(ciudades_mostradas))
print("mostrando otra ciudad...")
print(next(ciudades_mostradas))
print("mostrando otra ciudad...")