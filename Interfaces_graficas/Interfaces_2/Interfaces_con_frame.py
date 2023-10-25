#para crear interfaces en python se usa la librería tkinter
#se importa de la siguiente manera
from tkinter import *

raiz=Tk()

#aplicar titulo a la ventana
raiz.title("Mi titulo de ventana")

#Congelar  la redimención o el tamaño de la ventana
#se usa el metodo resizable y recibe dos parametros pueden ser true o False cada uno para poder modificar el tamaño
#raiz.resizable(False, False)

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


####################  INTERFACES II ##########################
#Creamos el frame para incluirlo en la raiz
mi_frame = Frame()
#Empaquetamiento del Frame
#mi_Frame.pack(fill=”valor”) 	‘x’, ‘y’, ‘both’, ‘none’
#mi_Frame.pack(expand=”valor”) 	0, 1, “True”, “False”
#mi_Frame.pack(side=”valor”) 	‘left’, ‘right’, ‘top’, ‘bottom’
#mi_frame.pack(side="bottom")
mi_frame.pack(fill='x',expand='1')
#grosor de borde
mi_frame.config(bd=18)
#cambiar el tipo de cursor --- tipos de cursores
#arrow, circle, clock, cross, dotbox, exchange, fleur, heart, man, mouse, pirate, plus, shuttle, sizing, spider, spraycan, star, target, tcross,trek
mi_frame.config(cursor="heart")

# List of cursors 
cursors =[ 
        "arrow", 
        "circle", 
        "clock", 
        "cross", 
        "dotbox", 
        "exchange", 
        "fleur", 
        "heart", 
        "man", 
        "mouse", 
        "pirate", 
        "plus", 
        "shuttle", 
        "sizing", 
        "spider", 
        "spraycan", 
        "star", 
        "target", 
        "tcross", 
        "trek"
] 

# Iterate through all cursors 
for cursor in cursors: 
    Button(raiz,text=cursor,cursor=cursor).pack() 

#Cambiar el tipo de borde
mi_frame.config(relief='sunken')
#darle color al frame
mi_frame.config(bg="red")
#darle tamaño al frame
mi_frame.config(width="650", height="300")




#mainloop es un bucle infinito para que se pueda quedar a la vista del usuario
raiz.mainloop()


################ IMPORTANTE #######################
#en este punto ya podemos ir a lka ubicacion del archivo y ejecutar con python con doble cli
#para ejecutarlo sin la consola detrás solo es cambiarle la extension al archivo de .py a .pyw
################ IMPORTANTE #######################
#VIDEO 44 pildoras
################ IMPORTANTE #######################