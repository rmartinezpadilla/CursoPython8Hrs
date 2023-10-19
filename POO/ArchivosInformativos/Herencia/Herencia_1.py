#herencia

class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f'Hola, soy {self.nombre} y estoy hablando...')
        

#forma correcta de la herencia en python
# en este caso vamos a heredar de la clase persona y vamos a crear una nueva clase

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo  = trabajo
        self.salario =  salario
        
miriam = Empleado("Miriam", 23, "Colombiana", "secretaria", 1250000)

print(miriam.nombre)

#Tambien heredamos los métodos de la clase padre, en este caso la clase Persona
miriam.hablar()
