from tkinter import *



raiz = Tk()

mi_frame = Frame(raiz, width =500, height = 400)
mi_frame.pack()

#creamos la variable nombre y le decirmos que sera una vartiable de tipo string
mi_nombre = StringVar()

#creamos el label
titulo_nombre = Label(mi_frame, text="Nombre:", fg="red", font=("Comic Sans MS", 12))

#usaremos grilla para definir la posicion de los elementos dentro de la ventana
#para uusaremos el método grid, para la posicion del elemento
titulo_nombre.grid(row=0, column=0, sticky=E, padx=15, pady=5)
#titulo_nomre.place(x=100, y=100)

#creamos una caja de texto
txt_nombre = Entry(mi_frame, textvariable=mi_nombre)
#txt_nombre.place(x=100, y=130)
#para uusaremos el método grid, para la posicion del elemento
txt_nombre.grid(row=0, column=1, sticky=E, padx=15, pady=5)
txt_nombre.config(justify="center")
#Para la ubicacion de los elementos podemos usar los metodos north, west, south, es decir se usan los puntos cardinales

titulo_apellido = Label(mi_frame, text="Apellido:", fg="red", font=("Comic Sans MS", 12))
titulo_apellido.grid(row=2, column=0,sticky=E, padx=15, pady=5)
txt_apellido = Entry(mi_frame)
txt_apellido.grid(row=2, column=1, sticky=E, padx=15, pady=5)
txt_apellido.config(justify="center")


titulo_password = Label(mi_frame, text="Password:", fg="red", font=("Comic Sans MS", 12))
titulo_password.grid(row=1, column=0,sticky=E, padx=15, pady=5)
txt_pass = Entry(mi_frame)
txt_pass.grid(row=1, column=1, sticky=E, padx=15, pady=5)
txt_pass.config(justify="center")
#ocultar caracteres de un input
txt_pass.config(show='*')

titulo_direccion = Label(mi_frame, text="Direccion:", fg="red", font=("Comic Sans MS", 12))
titulo_direccion.grid(row=3, column=0, sticky=E, padx=15, pady=5)
txt_direccion = Entry(mi_frame)
txt_direccion.grid(row=3, column=1, sticky=E, padx=15, pady=5)
txt_direccion.config(justify="center")

titulo_comentarios = Label(mi_frame, text="Comentarios:", fg="red", font=("Comic Sans MS", 12))
titulo_comentarios.grid(row=4, column=0, sticky=E, padx=15, pady=5)
txt_comentarios = Text(mi_frame, width=20, height=5)
txt_comentarios.grid(row=4, column=1, sticky=E, padx=15, pady=5)


#Creamos un scroll bar
scrolVertical = Scrollbar(mi_frame, command=txt_comentarios.yview)
#posicion dentro de la ventana
#adaptación del scroipbar dentro del txt comentarios
scrolVertical.grid(row=4, column=2,sticky="nsew")
#le ponemos el comportamiento deseado al scroll bar junto con la caja de comentarios
txt_comentarios.config(yscrollcommand=scrolVertical.set, fg="red", spacing1="7")

def codigoBoton():
    mi_nombre.set("Juan")

enviar = Button(raiz,text="Enviar", command=codigoBoton)
enviar.pack()


raiz.mainloop()