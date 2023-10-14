#creando una función que lance excepciones propias
#para eso usamos la palabra reservada raise
def evaludaEdad(edad):
    if edad < 0 :
        raise  TypeError("No se permiten edades negativas")
    if edad < 10 :
        return ("eres un niño")
    

print(evaludaEdad(-1))
    