mi_diccionario = {
'nombre' : "Rubén",
'edad' : 33,
'esta_feliz' : True,
'estatura' : 1.63,
'dato_repetido' : "Rubén"
}

#Keys - devuelve las claves
claves = mi_diccionario.keys()
print (claves)


#Get -  nos devuelve el valor de una clave, es decir lo que contiene
mi_valor = mi_diccionario.get("edad")
print (mi_valor)

#Pop - elimina un elemento del diccionario
mi_diccionario.pop("dato_repetido")
print(mi_diccionario)


#Clear - elimina  todos los elementos del diccionario
mi_diccionario.clear()
print(mi_diccionario)