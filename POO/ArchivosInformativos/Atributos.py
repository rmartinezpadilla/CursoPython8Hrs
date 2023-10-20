class Celular():
    #Método constructor de la clase
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

#objeto
mi_telefono_a = Celular("TCL", "65' pulgadas", "48MPX")
mi_telefono_b = Celular("Samsumg", "S 10", "48MPX")

print(mi_telefono_a.marca)
print(mi_telefono_b.marca)