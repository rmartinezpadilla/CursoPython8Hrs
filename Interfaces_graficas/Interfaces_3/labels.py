#crear y usar labels
#importamos la librería tkinter

from tkinter import *

root = Tk()

mi_frame = Frame(root, width =500, height = 400)

mi_frame.pack()

#creamos el label
mi_label = Label(mi_frame, text="Hola, esto es un ejemplo de label", fg="red", font=("Comic Sans MS", 18))

#empaquetamos el label para mostrarlo en la ventana
#mi_label.pack()
mi_label.place(x=100, y=200)

root.mainloop()