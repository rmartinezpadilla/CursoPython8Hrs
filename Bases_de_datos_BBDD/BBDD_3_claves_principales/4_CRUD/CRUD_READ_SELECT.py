import sqlite3

mi_conexion = sqlite3.connect("SegundaBaseDeDatos")

mi_apuntador = mi_conexion.cursor()

mi_apuntador.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Juguetería'")

datos=mi_apuntador.fetchall()

#print(datos)

for info in datos:
    print(info)

mi_conexion.commit()

mi_conexion.close()