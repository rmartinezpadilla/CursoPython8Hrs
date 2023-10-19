#crear dos clases principales (Persona y Estudiante)
#la clase Persona tendrá dos atributos nombre y edad y un médoto que me imprima el nombre y la edad de la persona
#la Clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional llamado grado, y un método que iomprima el grado del estudiante

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad =edad
    
    def dame_datos(self):
        return f'El nombre es: {self.nombre} y la edad es: {self.edad}'
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def dame_grado(self):
        return self.grado
    
obj_1 = Estudiante("Juan", 23, 10)

print(obj_1.dame_datos())
print(obj_1.dame_grado())