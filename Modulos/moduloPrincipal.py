#aqui llamamos todos los módulos que querramos, dependiendo la ruta donde se cuentren

#primero debemos importar el modulo donde se encuentra la funcion que queremos utilizar
#aqui practicamente lo que hacemos es crear un objeto de la clase en mención
#----> import modulo_saludar

#print(modulo_saludar.saluda_a("Juan"))

#otra forma de importar una clase y automaticamente asignar un nombre a dicha clase
#lo podemos hacer de la siguiente manera
#---> import modulo_saludar as m_saludar

#print(m_saludar.saluda_a("Juan"))

#otra forma de importar solo los métodos o el método que querramos utiizar de una clase solo debemos escribir la siguiente sentencia
# como podemos observar a continuación solo se pone  la palabra reservada from, el nombre del archivo (módulo) y se escribe el nombre del método a importar
# Si queremos importar varios métodos del mismo método solo debemos separarlos por comas (,)
from modulo_saludar import saluda_a

print(type(saluda_a))
print(saluda_a("Juan"))


#tambien cuando importamos solo un médoto o métodos especificos y queremos renombrarlos lo podemos hacer la siguiente manera
from modulo_saludar import saluda_a as yo_te_saludo

print(type(yo_te_saludo))
print(yo_te_saludo("Juan"))
