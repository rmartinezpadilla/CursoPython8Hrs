#importamos la librería re

import re

cadena ="Esto es un ejemplo de un texto, pero pueden exisitir varios ejemplos de lo mismo, ya que ejemplo con ejemplos no es lo mismo"

texto_buscar = "ejemplo"

#print(re.search("un", cadena))

# valor_encontrado = re.search(texto_buscar, cadena)

#usamos el metodo finall para buscar todas las veces que se encuentre nuestra texto dentro de la cadena
print(re.findall(texto_buscar, cadena))

print(len(re.findall(texto_buscar, cadena)))

# ---------------- OTRO EJERICIO -----------------


lista_datos=[
    'http://mail.t-evolvers.com/Default.net',
    'ftp://mail.t-evolvers.com/Default.ar',
    'http://mail.t-evolvers.com/Default.com',
    'ftp://mail.t-evolvers.com/Default.net'
]

#aplicamos los ajustes al metodo findall

for dato in lista_datos:
    if re.findall('^ftp', dato):
        print(dato)
        
        
# ---------------- OTRO EJERICIO -----------------


lista_datos=[
    'Compañía',
    'Empresa',
    'División',
    'Compañia'
]

#aplicamos los ajustes al metodo findall

for dato in lista_datos:
    if re.findall('Compañ[ií]a', dato):
        print(dato)