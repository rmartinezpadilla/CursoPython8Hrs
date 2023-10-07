ejemplo_con_dir = "mi ejemplo uno"
ejemplo_con_upper = "Mi eJempLo DOS"
ejemplo_con_lower = "Mi eJempLo TRES"
ejemplo_con_capitalize = "texto normal"
ejemplo_con_find = "esto es un ejemplo de una cadena relativamente amplia para poder buscar lo que se necesite dentro de ella"
ejemplo_con_index = "esto es un ejemplo de una cadena relativamente amplia para poder buscar lo que se necesite dentro de ella"
numero = "20"
alfa = "aqplapq10"

#DIR -  Devuelve la lista de atributos válidos dl objeto pasado
#nos muestra la cantidad de metodos que le puedo aplicar al objeto

print (dir(ejemplo_con_dir))


#UPPER -  Nos convierte una cadena de texto en mayusculas
print("imprimiendo en mayusculas " + ejemplo_con_upper.upper())


#LOWER -  Nos convierte una cadena de texto en minusculas
print("imprimiendo en minusculas " + ejemplo_con_lower.lower())

#CAPITALIZE - Nos convierte la primera letra en mayusculas
#primero convierte toda la cadena de texto en minusculas y lueco nos prone la primera mayusculas
print("escribiendo la primera letra en mayusculas->  " + ejemplo_con_capitalize.capitalize())

#FIND - se utiliza para buscar la posición de una subcadena de texto dentro de otra cadena
# devuelve -1 si no encuentra ninguna coincidencia (-1)
print(+ ejemplo_con_find.find("ente"))

#INDEX -  se utiliza para buscar la posición de una subcadena de texto dentro de otra cadena
# devuelve una excepción si no encuentra ninguna coincidencia (excepcion)
print(ejemplo_con_index.index("ente"))

#ISNUMERIC - validamos que el objeto sea un número
#se debe tener en cuenta que el valor debe estar en comillas, como una cadena de texto
es_numerico=numero.isnumeric()
print(es_numerico)

#ISAlPHA - si el objeto que le pasamos es númerico devuelve true
es_alpha = alfa.isalpha()
print(es_alpha)

#COUNT - devuelve el númnero de concurrencia de una subcadena de una cadena dada
#devuelve la cantidad de veces que coincida, en nuestro caso nos va a devolver la cantidad de veces que aparece la letra "a" en el texto
contar_coincidencias = ejemplo_con_find.count("a")
print(contar_coincidencias)

#LEN - cuenta la cantidad de caracteres de una cadena
#tener en cuenta que len no es un método, es una función, entonces recibe como parametro el objeto, ejemplo len(objeto_de_texto)
print(len(ejemplo_con_index))

#STARTSWITH -  Valida si una cadena de texto comienza por un valor en especifico, por ejemplo si se quiere saber como comienza una frase
#devuelve True en caso de que la comparación sea correcta, de lo contrario devuelve False
comienza_con = ejemplo_con_index.startswith("esto")
print(comienza_con)

#ENDSWITH -  Valida si una cadena de texto termina por un valor en especifico, por ejemplo si se quiere saber como termina una frase
#devuelve True en caso de que la comparación sea correcta, de lo contrario devuelve False
comienza_con = ejemplo_con_index.endswith("xyz")
print(comienza_con)

#REPLACE - reemplaza un valor por otro
cambia_el_valor = ejemplo_con_index.replace("ejemplo", "xxx")
print(cambia_el_valor)

#SPLIT -  nos devuelve como una lista la cadena de texto dada
#ejemplo - > ['Mi', 'eJempLo', 'DOS']
dame_split  = ejemplo_con_upper.split()
print(dame_split)