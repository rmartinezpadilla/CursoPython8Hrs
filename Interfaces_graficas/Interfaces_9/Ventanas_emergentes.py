# Las ventanas emergentes, cuadros de diálogo o simplemente Pop Ups, 
# sirven para mostrar o pedir información rápida al usuario. 
# Reciben ese nombre porque no forma parte de la ventana principal, 
# sinó que aparecen de golpe encima.
# La ventana emergente por excelencia es la MessageBox, 
# que sirve para mostrar un icono y un mensaje, pero tiene algunas variantes. 
# Desde la clásico ventana con la opción de aceptar, 
# la de alerta para informar de excepciones o errores, y las de aceptar o rechazar algo.
from tkinter import *
from tkinter import messagebox as MessageBox

def info():
    MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje

def alerta():
    MessageBox.showwarning("Hola!", "Hola mundo") # título, mensaje

def error():
    MessageBox.showerror("Hola!", "Hola mundo") # título, mensaje

def pregunta():
    #MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje
    resultado = MessageBox.askquestion("Salir","¿Está seguro que desea salir sin guardar?")
    if resultado == "yes":
        print("Salí de la aplicación")
        root.destroy()  # Destruir, alternativa a quit
    
def acept_o_cancelar():
    #MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje
    resultado = MessageBox.askokcancel("Salir", "¿Sobreescribir fichero actual?")

    if resultado == True:
        # Hacer algo
        #pass
        print("Estoy en la opcion aceptar del Sobreescribir del mensaje")
    
def reintentar_o_cancelar():
    #MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje
    resultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")

    if resultado == True:
        # Hacer algo
        #pass
        print("Estoy en la opcion reintentar del mensaje")
    
root = Tk()

Button(root, text = "Clícame para ver mensaje de información", command=info).pack()
Button(root, text = "Clícame para ver mensaje alerta", command=alerta).pack()
Button(root, text = "Clícame para ver mensaje de error", command=error).pack()
Button(root, text = "Clícame para ver mensaje de salir o continuar", command=pregunta).pack()
Button(root, text = "Clícame para ver mensaje de aceptar o cancelar", command=acept_o_cancelar).pack()
Button(root, text = "Clícame para ver mensaje de reintentar o cancelar", command=reintentar_o_cancelar).pack()
Button(root, text = "Clícame para Elegir un color", command=reintentar_o_cancelar).pack()
Button(root, text = "Clícame para abrir la ruta de un fichero", command=reintentar_o_cancelar).pack()
Button(root, text = "Clícame para salvar-guardar un fichero", command=reintentar_o_cancelar).pack()
Button(root, text = "Clícame para SALIR", command=root.quit).pack()

root.mainloop()
