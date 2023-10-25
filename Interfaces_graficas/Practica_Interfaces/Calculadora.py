from tkinter import *


raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

operacion = ""

resultado = 0
#-------------------PANTALLA--------------------

numero_pantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numero_pantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="red", fg="white", justify="right")

#------------------- métodos --------------------
def dato_boton(valor):
    global operacion
    
    if operacion !="":
        numero_pantalla.set(valor)
        operacion=""
    else:
        #obtengo lo que tiene la pantalla y agrego el nuevo número
        #dato_actual_pantalla = pantalla.get()
        numero_pantalla.set(numero_pantalla.get() + valor)

def suma(num):
    global operacion
    global resultado
    
    resultado += int(num)
    
    operacion = "suma"
    
    print(mensaje)
    numero_pantalla.set(resultado)
    

def el_resultado():
    
    global resultado
    
    numero_pantalla.set(resultado+int(numero_pantalla.get()))
    
    resultado = 0
    
    
    
#-------------------FILA 1--------------------
#Creamos y aplicamos las funciones lambda (importante en estos casos)
#donde debemnos usar este tipos de funciones donde debemos esperar que el usuario presione el boton
#por que si no, se ejecuta la funcion sin haber pulsado el botón
boton7 = Button(miFrame, text="7", width=3, command=lambda:dato_boton("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda:dato_boton("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda:dato_boton("9"))
boton9.grid(row=2, column=3)
botonmultiplicar = Button(miFrame, text="*", width=3)
botonmultiplicar.grid(row=2, column=4)
#-------------------FILA 2--------------------

boton4 = Button(miFrame, text="4", width=3, command=lambda:dato_boton("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda:dato_boton("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda:dato_boton("6"))
boton6.grid(row=3, column=3)
botonrestar = Button(miFrame, text="-", width=3)
botonrestar.grid(row=3, column=4)
#-------------------FILA 3--------------------

boton3 = Button(miFrame, text="3", width=3, command=lambda:dato_boton("3"))
boton3.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda:dato_boton("2"))
boton2.grid(row=4, column=2)
boton1 = Button(miFrame, text="1", width=3, command=lambda:dato_boton("1"))
boton1.grid(row=4, column=3)
botonsumar = Button(miFrame, text="+", width=3, command=lambda:suma(numero_pantalla.get()))
botonsumar.grid(row=4, column=4)
#-------------------FILA 4--------------------

#botonnulo = Button(miFrame, text="#--#", width=3)
#botonnulo.grid(row=5, column=1)
botoncero = Button(miFrame, text="0", width=3, command=lambda:dato_boton("0"))
botoncero.grid(row=5, column=1)
botoncoma = Button(miFrame, text=",", width=3, command=lambda:dato_boton(","))
botoncoma.grid(row=5, column=2)
botonigual = Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonigual.grid(row=5, column=3)
#botonigual.grid(row=5, column=2, columnspan=2)
botondividir = Button(miFrame, text="/", width=3)
botondividir.grid(row=5, column=4)


#------------------- métodos --------------------

    
raiz.mainloop()

##video 48