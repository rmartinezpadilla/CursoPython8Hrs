from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
  
root = Tk()

def elige_color():
    color = ColorChooser.askcolor(title="Elige un color")
    MessageBox.showinfo("El color elegido fué: ", {color} ) # título, mensaje


def dame_ruta():
    fichero = FileDialog.askopenfilename(title="Abrir un fichero")
    #print(fichero)
    MessageBox.showinfo("La ruta del archivo es: ", {fichero} ) # título, mensaje
    #----------------INICO COMENTARIO-----------------------
    # Como véis nos abre el cuadro de diálogo para gestionar ficheros en modo Abrir y nos devuelve la ruta. 
    # Y si no elegimos un fichero, se devuelve un valor vacío.
    # Sin embargo lo más interesante es que también podemos establecer otras opciones, 
    # por ejemplo un directorio inicial y un filtro de extensiones. 
    # Pero debéis tener cuidado con el directorio, ya que no todos los sistemas operativos utilizan el mismo tipo de rutas:
    #----------------FIN COMENTARIO-----------------------
    # file = FileDialog.askopenfilename(
    # initialdir="C:", 
    # filetypes=(
    #     ("Ficheros de texto", "*.txt"),
    #     ("Todos los ficheros","*.*")
    # ), 
    # title = "Abrir un fichero."
    # )

def guardar_fichero():
    fichero = FileDialog.asksaveasfile(
        title="Guardar un fichero", mode='w', defaultextension=".txt")

    if fichero is not None:
        fichero.write("Hola!")
        fichero.close()
            
Button(root, text = "Clícame para Elegir un color", command=elige_color).pack()
Button(root, text = "Clícame para abrir la ruta de un fichero", command=dame_ruta).pack()
Button(root, text = "Clícame para salvar-guardar un fichero", command=guardar_fichero).pack()
Button(root, text = "Clícame para SALIR", command=root.quit).pack()

root.mainloop()
