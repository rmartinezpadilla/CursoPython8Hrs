class empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo =  cargo
        self.salario = salario
        
    #esta funcion es muy buena
    def __str__(self) -> str:
        return "{} que trabaja como {} y tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)
    
listaEmpleados=[
    empleado("Lala", "Secretaria", 1100000),
    empleado("Juana", "Analist Quality", 3520000),
    empleado("Erick", "Developer", 5360000)
]

#aplicando la funcion lamda y filter para traer los empleados que tienen mayor salario

salarios_altos = filter(lambda empleado:empleado.salario>5000000, listaEmpleados)

for datos_obtenidos in salarios_altos:
    print(datos_obtenidos)