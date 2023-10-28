#importamos la librería de SQLite
import sqlite3

#creamos una conexión a la base de datos
#tener en cuenta que no la hemos creado, la crea al momento de ejecutar el programa
miConexion = sqlite3.connect("PrimeraBase")

# paso dos crear el cursor o puntero
miPuntero = miConexion.cursor()

#creamos una instruccion SQL
#miPuntero.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(30))")

#voy  practicar metiendola en un try except
#esto con el fin de validar si la base de datos existe

try:
    miPuntero.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(30))")
    print("La base de datos no existía y fué creada correctamente.")  
except:
    print(f'La base de datos esta creada')
#else:  
    #Insertar datos en la tabla
 #   miPuntero.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15000, 'DEPORTES')")
finally:
	# Este bloque se ejecutara siempre
    #confirmamos la insercion o los cambios que vayamos a hacer en la tabla o en la base de datos
    #para esto usamos la conexion
    miPuntero.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15000, 'DEPORTES')")
    miConexion.commit()

#cerramos la conexión
miConexion.close()