import sqlite3

mi_conexion = sqlite3.connect("GestionData")

mi_apuntador = mi_conexion.cursor()

#agregamos al campo que no queremos que se repita la información  la clusula UNIQUE
#se pueden agregar en todos los campos que creamos convenientes
try:
    mi_apuntador.execute("CREATE TABLE PRODUCTOS(CODIGO_PRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_PRODUCTO VARCHAR(50) UNIQUE, PRECIO INTEGER, SECCION VARCHAR(30))")   
except:
    print("La tabla ya exisitía")

finally:
    #Creamos una tupla para insertar varios registros a la tabla
    mis_productos=[
        ("Jean", 55000, "Casual"),
        ("Cuchara", 2500, "Hogar"),
        ("Camión", 60000, "Juguetería"),
        ("Peinilla", 1500, "Belleza"),
        ("Puerta principal en madera", 90000, "Carpintería"),
        ("Clavos", 200, "Carpintería")
    ]
    #AQUI DEBEMOS PONER LOS 4 INTERROGANTES EN EL QUERY YA QUE EL PK ES AUTOINCREMENTABLE Y NO SE PASA
    #en este caso quitamos un interrogante y ahi ponemos la palabra reservada null
    mi_apuntador.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", mis_productos)
    #Confirmamos la ejecución de SQL
    mi_conexion.commit()
    print("Insertando datos")


mi_conexion.close()