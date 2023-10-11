#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
# vive en <dirección> y su número de teléfono es <teléfono>

#datos = dict.fromkeys(["nombre", "edad", "direccion", "telefono"])
datos = ()
def llenandoDiccionario():
    nombre = input('¿Cómo te llamas? ')
    edad = input('¿Cuántos años tienes? ')
    direccion = input('¿Cuál es tu dirección? ')
    telefono = input('¿Cuál es tu número de teléfono? ')
    datos = {
                "nombre" : nombre,
                "edad"   : edad,
                "direccion": direccion,
                "telefono" : telefono
            }
    return datos

print(type(llenandoDiccionario()))



