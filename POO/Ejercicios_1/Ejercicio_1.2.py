class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
  
    def estudiar(self):
        print(f'Estudiando contigo {self.nombre}')
        
#juan = Estudiante("Juan", 23, 6)
nombre = input("Dime el nombre: ")
edad = input("Dime la edad: ")
grado = input("Dime el grado: ")

alumno = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n
      Nombre: {alumno.nombre} \n
      Edad: {alumno.edad} \n
      Grado: {alumno.grado} \n            
      """)


while True:
    estudia = input()
    if(estudia.lower() == "estudiar"):
        alumno.estudiar()