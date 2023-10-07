#LIST -  Crea una lista ( es una función )
mi_lista = list(["dato 1", "dato 2", "dato 3", "dato 4", 30, False])
print(mi_lista)

#-------- METODOS-------#
#LEN -  Cuenta la cantidad de elementos de una lista
cantiad_elementos_de_la_lista = len(mi_lista)
print(cantiad_elementos_de_la_lista)

#APPEND - Agerga un elemento a la lista
mi_lista.append("otro elemento")
print(mi_lista)

#INSERT - Agrega un elemento a la lista en el indice especificado y el valor a insertar
mi_lista.insert(1,"insertado elmento")
print(mi_lista)

#EXTEND - Agrega varios elementos  a la lista
mi_lista.extend(["Extend 1", True, "Rubén"])
print(mi_lista)

#POP -  elimina un elemento de una lista, pide indice y devuelve el valor
mi_lista.pop(4)
print(mi_lista)

#REMOVE - Remueve un elemento de una lista, pide valor
#si le pasamos un valor que no existe dentro de la lista lanza una excepcion
mi_lista.remove("Rubén")
print(mi_lista)

#SORT - ordena una lista de forma ascendente a descendente
#funciona solo con listas de números
#si usamos el parametro reserverse =  true, ordenamos la lista en reversa
#mi_lista.sort()
#print()

#REVERSE - invierte los elementos de una lista


#CLEAR - elimina todos los elementos de una lista
mi_lista.clear()
print(mi_lista)

#ver todos los metodos o acciones que puedo realizar con una lista
print(dir(mi_lista))