class miclase:
    def __init__(self):
        #escribimos un atributo privado
        self.__miatributoPrivado = "Hola"

objeto = miclase()
#no debería mostrar nada ya que es privado interno y externamente
print(objeto.__miatributoPrivado)