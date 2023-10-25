from tkinter import * 

root =Tk()

root.title("Ejemplo")

playa = IntVar()
montan_a = IntVar()
turismo_rural = IntVar()
root.iconbitmap('C:/Users/Equipo/Desktop/Curso Python 8hrs/Interfaces_graficas/interfaces_7/img/Viajando.ico')

def opcion_viaje():
    opcion_escogida = ""
    
    if playa.get()==1:
        opcion_escogida+=" Playa "
    if montan_a.get()==1:
        opcion_escogida+=" Montaña "
    if turismo_rural.get()==1:
        opcion_escogida+=" Turismo Rural "
    
    mensaje.config(text=opcion_escogida)
# img = PhotoImage(file="C:/Users/Equipo/Desktop/Curso Python 8hrs/Interfaces_graficas/interfaces_7/img/Viajando.ico")
# can = Canvas(root)
# can.pack(fill=BOTH)
# can.create_image(20, 20, image=img, anchor=NW)

frame = Frame(root)
frame.pack()
Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcion_viaje).pack()
Checkbutton(frame, text="Monteña", variable=montan_a, onvalue=1, offvalue=0, command=opcion_viaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismo_rural, onvalue=1, offvalue=0, command=opcion_viaje).pack()

mensaje = Label(frame)
mensaje.pack()
root.mainloop()