from tkinter import *
root = Tk()

#con este metodo le decimos a la variable que va tomar valores de tipo entero 
#para los casos de string usamos la funcion StrVar()
varOpcion = IntVar()


# def que_tene_opcion():
#     print(varOpcion)

def imprimir():
    print(varOpcion.get())


def mostrar():
    #print(varOpcion.get())
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegido masculino")
    elif varOpcion.get()==2:
        etiqueta.config(text="Has elegido femenino")
    else:
        etiqueta.config(text="No sabes si eres Gay")
    


Label(root, text="Género: ").pack()
#creando un radio button
Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=mostrar).pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=mostrar).pack()
Radiobutton(root, text="No sabes", variable=varOpcion, value=3, command=mostrar).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()