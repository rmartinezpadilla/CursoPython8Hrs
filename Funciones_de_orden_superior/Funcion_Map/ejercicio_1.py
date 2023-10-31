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

def calculo_comision(empleado):
    empleado.salario=empleado.salario*1.03
    return empleado

#aplicando la funcion map podremos aplicar la funcion a un grupo de objetos y así aplicar u obtener lo que dice la funcion
listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for datos_obtenidos in listaEmpleadosComision:
    print(datos_obtenidos)    



