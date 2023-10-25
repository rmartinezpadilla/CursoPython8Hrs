#para crear interfaces en python se usa la librería tkinter
#se importa de la siguiente manera
from tkinter import *

raiz=Tk()

#aplicar titulo a la ventana
raiz.title("Mi titulo de ventana")

#Congelar  la redimención o el tamaño de la ventana
#se usa el metodo resizable y recibe dos parametros pueden ser true o False cada uno para poder modificar el tamaño
raiz.resizable(False, False)

#cambiar color de la raiz
raiz.config(bg="yellow")

#cambiar icono de la ventana debe ser lo mas pequeño posible
#raiz.iconphoto()
#raiz.iconphoto(False, raiz.PhotoImage(file='icono\mi_ico.png'))
#photo = PhotoImage(file = "mi_icono.ico")
#raiz.iconphoto(False, photo)
#raiz.iconbitmap('\icono\mi_icono.png')
raiz.iconbitmap('C:/Users/Equipo/Desktop/Curso Python 8hrs/Interfaces_graficas/Interfaces_1/img/mi_icono.ico')


#Definir el tamaño de la ventana
raiz.geometry('650x350')


#mainloop es un bucle infinito para que se pueda quedar a la vista del usuario
raiz.mainloop()


################ IMPORTANTE #######################
#en este punto ya podemos ir a lka ubicacion del archivo y ejecutar con python con doble cli
#para ejecutarlo sin la consola detrás solo es cambiarle la extension al archivo de .py a .pyw
################ IMPORTANTE #######################