#creando diccionario con la función dict()
mi_diccionario_1 = dict(nombre="juan", apellido="perez", edad=23)
print(mi_diccionario_1)
print(mi_diccionario_1["nombre"])

#las listas no pueden ser claves y usamos frozenset para meter conjuntos dentro de un diccionario
mi_diccionario_2 = {frozenset(["Juan", "perez"]): "Otro dato externo al conjunto"}
print(mi_diccionario_2)

#creando diccionarios con fromkeys()
#usando la función fromkeys creamos un diccionario vacío, es decir, se crean las claves pero sin valor alguno
mi_diccionario_3 =  dict.fromkeys(["nombre", "apellidos", "edad"])
print(mi_diccionario_3)

#de esta manera imprimimosu una clave en especifico
print(mi_diccionario_3["nombre"])

#otra forma interesante de crear diccionarios con fromkeys(), es iterar el primer parametro y a cada letra le va a dar un valor
#el valor será el segundo parametro, si no se pone ese valor (el segundo parametro) por defecto los crea nulos

#EJEMPLO SIN SEGUNDO PARAMETRO
mi_diccionario_4 = dict.fromkeys("ABCDF")
print(mi_diccionario_4)

#EJEMPLO CON EL  SEGUNDO PARAMETRO
mi_diccionario_5 = dict.fromkeys("ABCDF", "ejemplo")
print(mi_diccionario_5)