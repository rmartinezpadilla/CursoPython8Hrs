#importamos la librería re

import re

cadena ="Esto es un ejemplo de un texto"

texto_buscar = "ejemplo"

#print(re.search("un", cadena))

valor_encontrado = re.search(texto_buscar, cadena)

#usamos el metodo start
print(valor_encontrado.start())



#una  forma de validar (nunca había visto el "is nor None")

# if re.search("Esto", cadena) is not None:
#     print("He encontrado el texto")
# else:
#     print("No he encontrado el texto")
    
