import sqlite3

mi_conexion = sqlite3.connect("SegundaBaseDeDatos")

mi_apuntador = mi_conexion.cursor()

#pedimos los datos de entrada

name_product = input("dame el nombre del producto que quieres actualizar: ")
nuevo_precio = input("dame el nuevo valor del producto: ")

mi_apuntador.execute(f"UPDATE PRODUCTOS SET PRECIO={nuevo_precio} WHERE NOMBRE_ARTICULO='{name_product}'")

#Columna afectada
col_afectada = mi_apuntador.rowcount

if col_afectada > 0:
    print(f'Precio del producto {name_product} actualizados correctamente')
else:
    print("algo salió mal")



#print(col_afectada)

mi_conexion.commit()

mi_conexion.close()