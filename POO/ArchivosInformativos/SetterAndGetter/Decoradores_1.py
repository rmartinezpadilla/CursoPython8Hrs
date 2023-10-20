# #aplicando método getter  and setter para acceder a las propiedades de una clase desde dentro o desde afuer de ella misma
# #Usando decoradores

# class Persona:
#     def __init__(self, nombre, edad):
#         self._nombre = nombre
#         self._edad = edad
        
#     def get_nombre(self):
#         return self._nombre
    
#     def set_nombre(self, nombre):
#         self._nombre = nombre
    
#     def get_edad(self):
#         return self._edad
    
#     def set_edad(self, edad):
#         self._edad = edad


def decorador(funcion):
    def funcion_modificada():
        print ("esto ANTES de tomar la funcion")
        funcion()
        print ("esto DESPUÉS de tomar la funcion")
    return funcion_modificada

#usamos el docorador, se va a ejecutar antes
#tener en cuenta que es el nombre de la función decoradora
@decorador
def saludo():
    print("hola soy la funcion saludo")

saludo()