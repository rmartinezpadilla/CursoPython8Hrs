import sqlite3

mi_conexion = sqlite3.connect("GestionProductos")

mi_puntero = mi_conexion.cursor()

try:
    mi_puntero.execute("CREATE TABLE PRODUCTOS(CODIGO_PRODUCTO VARCHAR(4) PRIMARY KEY, NOMBRE_PRODUCTO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(30))")   
except:
    print("La tabla ya exisitía")

finally:
    #Creamos una tupla para insertar varios registros a la tabla
    mis_productos=[
        ("OBJ01","Jean", 55000, "Casual"),
        ("OBJ02","Cuchara", 2500, "Hogar"),
        ("OBJ03","Camión", 60000, "Juguetería"),
        ("OBJ04","Peinilla", 1500, "Belleza"),
        ("OBJ05","Puerta principal en madera", 90000, "Carpintería"),
        ("OBJ06","Clavo", 200, "Carpintería")
    ]
    mi_puntero.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", mis_productos)

    #Confirmamos la ejecución de SQL
    mi_conexion.commit()
    print("Insertando datos")

mi_conexion.close()