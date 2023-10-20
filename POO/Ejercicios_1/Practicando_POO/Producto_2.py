# 1. Crear una Clase Producto con los siguientes atributos:
# - codigo
# - nombre
# - precio 
#Creale, su constructor, getter y setter y una funcion llamada calcular_total, donde le pasaremos unas unidades y nos debe calcular el precio final.

#2. Añadir una clase pedido que tiene como atributos:
#    - lista de productos
#    - lista de cantidades
#   Añade las siguiente funcionalidad:
#    - total_pedido: muestra el precio final del pedido
#    - mostrar_productos: muestra los productos del pedido

class Producto:   
    codigo = 0
    nombre = ""
    precio = 0
    
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
    
    #Para definir los métodos Get se pone la palabra reservada  (Decorador)  @property    
    #Definamos un método get
    @property
    def codigo(self):
        return self.codigo
    
    #Para definir los métodos Setter no se pone de la siguiente manera @nombreDelAtributo.setter
    #Ejemplo @codigo.setter
    #Definamos un método set, el decorador debe llevar el mismo nombre del método
    @codigo.setter
    def codigo(self, valor):
        self.codigo = valor
    
    #Para definir los métodos Get se pone la palabra reservada (Decorador) @property    
    #Definamos un método get
    @property
    def nombre(self):
        return self.nombre
    
    #Para definir los métodos Setter no se pone de la siguiente manera @nombreDelAtributo.setter
    #Ejemplo @codigo.setter
    #Definamos un método set
    @nombre.setter
    def nombre(self, valor):
        self.nombre = valor
        
    #Para definir los métodos Get se pone la palabra reservada  (Decorador) @property    
    #Definamos un método get
    @property
    def precio(self):
        return self.precio
    
    #Para definir los métodos Setter no se pone de la siguiente manera @nombreDelAtributo.setter
    #Ejemplo @codigo.setter
    #Definamos un método set
    @precio.setter
    def precio(self, valor):
        self.precio = valor
#una funcion llamada calcular_total, donde le pasaremos unas unidades y nos debe calcular el precio final.

    def calcular_total(self, unidades):
        total = self.precio * unidades
        return total
    
    def misDatos__str__(self):
        return 'Codigo: ' + str(self.codigo) + ' , nombre: ' + str(self.nombre) + ', precio : '+ str(self.precio)
    

class Pedido:

    __productos = []
    __cantidades = []

    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades

    def total_pedido(self):
        total = 0

        for (p,c) in zip(self.__productos, self.__cantidades):
            total = total + p.calcular_total(c)

        return total

    def mostrar_productos(self):

        for (p,c) in zip(self.__productos, self.__cantidades):
            print('Producto: ' + p.get_nombre() + ', Cantidad: ' + str(c))



p1 = Producto(1, "producto 1", 5)
p2 = Producto(2, "producto 2", 15)
p3 = Producto(3, "producto 3", 25)

productos = [p1,p2,p3]
cantidades = [5, 10, 2]


pedido = Pedido(productos, cantidades)

print('Total pedido: '+ str(pedido.total_pedido()))

pedido.mostrar_productos()