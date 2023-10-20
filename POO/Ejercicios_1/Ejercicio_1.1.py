class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
juan = Estudiante("Juan", 23, 6)

print(juan.edad)