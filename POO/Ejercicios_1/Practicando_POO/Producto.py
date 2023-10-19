# 1. Crear una Clase Producto con los siguientes atributos:
# - codigo
# - nombre
# - precio 
#Creale, su constructor, getter y setter y una funcion llamada calcular_total, donde le pasaremos unas unidades y nos debe calcular el precio final.

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
   # @property
   # def codigo(self):
    #    return self.codigo
    
    #Para definir los métodos Setter no se pone de la siguiente manera @nombreDelAtributo.setter
    #Ejemplo @codigo.setter
    #Definamos un método set, el decorador debe llevar el mismo nombre del método
    #@codigo.setter
    #def codigo(self, valor):
    #    self.codigo = valor
    
    #Para definir los métodos Get se pone la palabra reservada (Decorador) @property    
    #Definamos un método get
   # @property
    #def nombre(self):
    #    return self.nombre
    
    #Para definir los métodos Setter no se pone de la siguiente manera @nombreDelAtributo.setter
    #Ejemplo @codigo.setter
    #Definamos un método set
    #@nombre.setter
    #def nombre(self, valor):
    #    self.nombre = valor
        
    #Para definir los métodos Get se pone la palabra reservada  (Decorador) @property    
    #Definamos un método get
    #@property
    #def precio(self):
    #    return self.precio
    
    #Para definir los métodos Setter no se pone de la siguiente manera @nombreDelAtributo.setter
    #Ejemplo @codigo.setter
    #Definamos un método set
    #@precio.setter
    #def precio(self, valor):
    #    self.precio = valor
#una funcion llamada calcular_total, donde le pasaremos unas unidades y nos debe calcular el precio final.

    def calcular_total(self, unidades):
        total = self.precio * unidades
        return total
    
    def misDatos__str__(self):
        return 'Codigo: ' + str(self.codigo) + ' , nombre: ' + str(self.nombre) + ', precio : '+ str(self.precio)
    

objeto_1 = Producto(1, "Tarjeta", 2650)
calculo = objeto_1.calcular_total(36)

print(calculo)

print(objeto_1.misDatos__str__())
