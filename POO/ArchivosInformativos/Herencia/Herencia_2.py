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

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas  = notas
        self.universidad =  universidad
        
juan = Estudiante("Juan", 23, "Colombiano", 4.3, "Universidad de córdoba")

print(juan.nombre)

#Tambien heredamos los métodos de la clase padre, en este caso la clase Persona
juan.hablar()

#Si quieremos llamar a un método de la clase padre dentro de otro método de la clase hijo usamos la alabra reservada super().
#y después del punto llamamos al método