#EN ESTA PARTE DEL CURSO LO QUE HAREMOS ES INSTALAR PAQUETES DENTRO DE LA RAIZ DEL PROYECTO
# CON EL FIN DE PODER UTULIZAR PAQUETES EN CUALQUIER LUGAR DEL PROYECTO
# A ESTA PARTE SE LE LLAMA PAQUETES DISTRIBUBLES
#Para esto se crea un archivo llamado setup.py dentro de la raiz de tu proyecto

#para el ejemplo el archivo quedaría así de la siguiente manera

##OJO SIN ALMUADILLA SIN COMENTAR, ESTO PARA EL EJEMPLO

# ------------->

#from setuptools import setup

#setup(
    
#     name = "paquetecalculos",
#     version = "1.0",
#     description = "paquete de redondeo y potencias",
#     author = "Rubén",
#     url = "www.ejemplos.com",
#     packages =["calculos","calculos.redondeo_y_potencia"] ruta del paquete separados por comas
# )

# <--------------

#después de hacer esos pasos ir a al arrchivo desde la consola CMD y ahi abrir el archivo setup.py
#usando los sigueintes comandos
#python setup.py sdist

#esto se usa para poder compartirlo
