# En esta lección vamos a aprender a crear un menú superior de toda la vida con varias secciones.
# El primer widget menú que creamos hace referencia a la barra de menú, de ahí que se le suele llamar menubar:

from tkinter import *

# Configuración de la raíz
root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

#Una vez creada la barra podemos comenzar a añadir submenús y comandos. 
# Empecemos con los submenús:

filemenu = Menu(menubar, tearoff=0)
# Bien ya tenemos nuestra barra con los 3 submenús funcionando bien, 
# pero ocurre algo raro, nos aparece una especie de elemento por defecto. 
# Podemos hacer que desaparezca si indicamos el parámetro tearoff=0:
filemenu.add_command(label="Nuevo")
# Ahora sí que lo tenemos bien, ¿pero está demasiado vacío no? 
# Vamos a añadir comandos de ejemplo en nuestros submenús:
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
# También podemos agregar un separador y un comando de salir con root.quit:
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

#Una vez creada la barra podemos comenzar a añadir submenús y comandos. 
# Empecemos con los submenús:

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

#Una vez creada la barra podemos comenzar a añadir submenús y comandos. 
# Empecemos con los submenús:

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

#Ya tenemos los submenús, pero todavía nos falta añadirlos a la barra de menú:
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Finalmente bucle de la aplicación
root.mainloop()
