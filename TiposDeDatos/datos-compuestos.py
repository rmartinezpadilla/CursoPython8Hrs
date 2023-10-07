#creando una lista
mi_lista = ["Rubén", "Aprendíz", True, 1.36]

#modificando la lista
mi_lista = ["Rubén", "Aprendíz", True, 1.63]

#modificando un campo de la lista
mi_lista[0] = "Mario"

#imprimiendo la lista
print(mi_lista)
#-------------------------------------------------------#
#creando una tupla, tener en cuenta que se crea con parentésis
tupla = ("Rubén", "Aprendíz", True, 1.36)

#modificando la tupla, no se puede modificar una tupla
#tupla[1]="Maestro"

#imprimiendo la tupla
print(tupla)

#-------------------------------------------------------#

#creando un conjunto, tener en cuenta que se crea con llaves
mi_conjunto = {"Rubén", "Aprendíz", True, 1.36}

#modificando el conjunto, no se puede modificar un campo del conjunto
#   mi_conjunto[1]="Maestro"
#no permite repetir valores (nunca los muestra)
#al momento de imprimir los conjuntos los muestra en desorden en cada en ejecución

#imprimiendo el conjunto
print(mi_conjunto)

#-------------------------------------------------------#

#creando un diccionario (dict), tener en cuenta que se crea como un Json
mi_diccionario = {
'nombre' : "Rubén",
'edad' : 33,
'esta_feliz' : True,
'estatura' : 1.63,
'dato_repetido' : "Rubén"
}

#imprimiendo un campo con el nombre de dicho campo del diccionario
print(mi_diccionario['nombre'])

#modificando el conjunto, no se puede modificar un campo del conjunto
#   mi_conjunto[1]="Maestro"
#no permite repetir valores (nunca los muestra)
#al momento de imprimir los conjuntos los muestra en desorden en cada en ejecución

#imprimiendo el conjunto
print(mi_diccionario)