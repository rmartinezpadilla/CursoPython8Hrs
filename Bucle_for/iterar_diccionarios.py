mi_diccionario = {
    "nombre":  "juan",
    "apellido": "perez"
    }

#recorrer un diccionario con for y la funcion items()

for datos in mi_diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es {value}')
print(mi_diccionario)