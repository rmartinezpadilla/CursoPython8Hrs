#en este archivo vamos a ver la forma de eexcepciones que podemos hacer en python

def divide(numeroa, numerob):
    try:
        return numeroa/numerob
    #en este caso ponemos el nombre del error por que lo conocemos
    #lo recomendable es que sea de manera general, es decir, para cualquier error
    except ZeroDivisionError:
        return "no se puede dividir por cero 0"


#usamos try y exception

print(divide(10,0))
##si sabemos manejar la excepcion debe mostrar el siguiente mensaje


print("sobrepasé la excepción")