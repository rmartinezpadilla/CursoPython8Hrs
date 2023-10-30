import sqlite3

mi_conexion = sqlite3.connect("SegundaBaseDeDatos")

mi_puntero = mi_conexion.cursor()

#Obtener datos de la base de datos
mi_puntero.execute("SELECT * FROM PRODUCTOS")

mis_datos_lista = mi_puntero.fetchall()

#print(mis_datos_lista)

for data in mis_datos_lista:
    print(f'Producto: {data[0]}, Precio: {data[1]}, Sección: {data[2]}')

mi_conexion.close()