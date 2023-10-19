#método de resolución de orden
#la prioridad que le da python al orden de los métodos y atributos en la herencia

class A:
   # def prueba(self):
    #    return "estoy desde A"
    pass

class B(A):
    #def prueba(self):
    #    return "estoy desde B"
    pass
    
class C:
    def prueba(self):
        return "estoy desde C"
    
class D(B,C):
    #def prueba(self):
    #    return "estoy desde D"
    pass
    

objeto = D()

print(objeto.prueba())

#Conocer la jerarquía
print(D.mro())