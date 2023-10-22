#metodos especiales

class Persona:
    def __init__(self, nombre, edad):
        self.nombre =nombre
        self.edad = edad
    
    #mostrar esta informacion solo llamando al objeto (1)
    #se usa str solo para mostrar la información
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    #otro metodo especial es el repr (2)
    def __repr__(self):
        return f'Persona("{self.nombre}","{self.edad}")'
    
     #otro metodo especial es el repr (3)
     #aqui definimos como se van a sumar los objetos cuando usemos esté metodo especial __add__
    def __add__(self, otro):
        nuevo_dato = self.nombre + otro.nombre
        return Persona(self.nombre+otro.nombre,nuevo_dato)
    
    

obj_1 = Persona("Juan", 23)

#mostrar el objeto con el metodo especial __str__(1)
print(obj_1)

#mostrar el objeto con el metodo especial __repr__(2)
# pero en este caso en especial podemos acceder a los atributos propios del objeto, ejemplo:
obj_2 = Persona("Elena", 60)
representacion = repr(obj_2)
atributo = eval(representacion)
print(atributo.edad)

#realizar la adicion de otro objeto usanto el metodo especial __add__(2)
#usamos los dos objetos creados en los pasos anteriores
nuevo_nombre = obj_1 + obj_2

print(nuevo_nombre.nombre)
