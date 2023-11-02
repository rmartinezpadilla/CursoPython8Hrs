#importamos la librería re

import re

cadena ="Esto es un ejemplo de un texto"

print(re.search("un", cadena))

#una  forma de validar (nunca había visto el "is nor None")

if re.search("Esto", cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")
    
