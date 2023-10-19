#herencia Multiple

class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        return(f'Hola, soy {self.nombre} y estoy hablando...')
        

class Artista():
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return (f'{self.habilidad}')

#aplicando herencia multiple        
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        #super().__init__(nombre, edad, nacionalidad)
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        return f'Mi nombre es: {self.nombre} y mi habilidad es {super().mostrar_habilidad()} y trabajo en {self.empresa}' 

eduardo = EmpleadoArtista("Eduardo", 29, "Colombiano", "tocar acordeón", "6000000", "enerBit")

print(eduardo.mostrar_habilidad())
print(eduardo.presentarse())

#Validar si una clase es subclase de otra

herencia = issubclass(EmpleadoArtista, Artista)

print(herencia)