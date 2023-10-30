from tkinter import *
from tkinter import messagebox as MessageBox
import sqlite3
import bcrypt

#----------------- METODOS -------------------------------------
def info_connect():
    MessageBox.showinfo("Te has conectado a la base de datos") # título, mensaje

def pregunta_salir():
    #MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje
    resultado = MessageBox.askquestion("Salir","¿Está seguro que desea salir?")
    if resultado == "yes":        
        raiz.destroy()  # Destruir, alternativa a quit
    
def conectar_crear_bbdd():
    #creamos una conexión a la base de datos
    #tener en cuenta que no la hemos creado, la crea al momento de ejecutar el programa
    miConexion = sqlite3.connect("Usuarios")
    miPuntero = miConexion.cursor()
    
    
    try:
        miPuntero.execute("CREATE TABLE DATOSUSUARIOS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_USUARIO VARCHAR(50), PASSWORD VARCHAR(50), APELLIDO VARCHAR(50), DIRECCION VARCHAR(50), COMENTARIOS VARCHAR(100))")      
        MessageBox.showinfo("Información","La base de datos fué creada correctamente.") # título, mensaje         
    except:
        MessageBox.showwarning("Alerta!","La base de datos estaba ya creada") # título, mensaje                    
        
    miConexion.commit()
    miConexion.close()

def valida_campos_vacios():
    if mi_nombre.get() == "":
        return True
    elif mi_passwd.get() == "":
        return True
    elif mi_apellido.get()== "":
        return True
    elif mi_direccion.get() == "":
        return True
    else:
        return False

def borrar_campos():    
    mi_id.set("")
    mi_nombre.set("")
    mi_passwd.set("")
    mi_apellido.set("")
    mi_direccion.set("")
    #para el cuadro de texto hacemos lo siguiente
    txt_comentarios.delete(1.0, END)

def almacenar_informacion():
    miConexion = sqlite3.connect("Usuarios")
    miPuntero = miConexion.cursor()
    
    # mis_datos=[
    #     (mi_nombre.get(), mi_passwd.get(), mi_apellido.get(), mi_direccion.get())
    # ]
    #se usa excecutemany cuando se le va a pasar un parametro a la funcion    
    #miPuntero.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?,?,?)", mis_datos)
    # if mi_nombre.get() == "":
    #     MessageBox.showerror("Ojo!","Todos los campos del formulario deben estar devidamente diligenciados.") # título, mensaje                    
    # elif mi_passwd.get() == "":
    #     MessageBox.showerror("Ojo!","Todos los campos del formulario deben estar devidamente diligenciados.") # título, mensaje
    # elif mi_apellido.get()== "":
    #     MessageBox.showerror("Ojo!","Todos los campos del formulario deben estar devidamente diligenciados.") # título, mensaje
    # elif mi_direccion.get() == "":
    #     MessageBox.showerror("Ojo!","Todos los campos del formulario deben estar devidamente diligenciados.") # título, mensaje
    
    if valida_campos_vacios():
        MessageBox.showerror("Ojo!","Todos los campos del formulario deben estar devidamente diligenciados.") # título, mensaje
    else:       
    #en este caso se usa excecute solamente por que le pasamos los datos de una en en script
        mi_clave_cifrada = mi_passwd.get().encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(mi_clave_cifrada, salt).decode()
                       
        # miPuntero.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'"+ mi_nombre.get() +
        #                     "','"+ str(hashed) +
        #                     "','"+ mi_apellido.get() +"','"+ mi_direccion.get() +
        #                     "','"+ txt_comentarios.get("1.0", END) +"')")
        
        #------------------otra forma de hacerlo-----------------------
        datos =  mi_nombre.get(), hashed, mi_apellido.get(), mi_direccion.get(), txt_comentarios.get("1.0", END)
        miPuntero.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL, ?,?,?,?,?)", (datos))
        
        miConexion.commit()
        
        #Columna afectada
        col_afectada = miPuntero.rowcount
        if col_afectada > 0:
            MessageBox.showinfo("Información","Datos insertados correctamente!") # título, mensaje        
            borrar_campos()
        else:
            MessageBox.showerror("Error","Algo salió mal!") # título, mensaje
    
    miConexion.close()

def obtener_datos()    :
    miConexion = sqlite3.connect("Usuarios")
    miPuntero = miConexion.cursor()
    
    if mi_id.get() == "":
        MessageBox.showerror("Error",f"El campo ID está vacío!") # título, mensaje
    else:
        miPuntero.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + mi_id.get())
        
        datos_de_usuario = miPuntero.fetchall()
        
        #print(type(datos_de_usuario))
        
        if len(datos_de_usuario) > 0 :            
            
            for info in datos_de_usuario:
                mi_id.set(info[0])
                mi_nombre.set(info[1])
                mi_passwd.set(info[2])
                mi_apellido.set(info[3])        
                mi_direccion.set(info[4])
                #usamos lo siguiente para alimentar el campo Text
                txt_comentarios.insert(1.0, info[5])
        else: 
            MessageBox.showerror("Error",f"La consulta no trajo ninguna información!") # título, mensaje
    
    miConexion.commit()
    miConexion.close()        

def eliminar_registro():
    miConexion = sqlite3.connect("Usuarios")
    miPuntero = miConexion.cursor()
    
    if mi_id.get() == "":
        MessageBox.showerror("Error",f"el campo ID está vacío!") # título, mensaje
    else:
        miPuntero.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + mi_id.get())
    
        miConexion.commit()
    
        #Columna afectada
        col_afectada = miPuntero.rowcount

        if col_afectada > 0:
            MessageBox.showinfo("Información",f"Registo con el id {mi_id.get()} eliminado correctamente!") # título, mensaje    
        else:
            MessageBox.showerror("Error",f"el id {mi_id.get()} no existe!") # título, mensaje
    
    miConexion.close()
    
def actualizar_registro():
    miConexion = sqlite3.connect("Usuarios")
    miPuntero = miConexion.cursor()
    
    # miPuntero.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + mi_nombre.get() +
    #       "', PASSWORD='" + mi_passwd.get() +
    #       "', APELLIDO='" + mi_apellido.get() +
    #       "', DIRECCION='" + mi_direccion.get() +
    #       "', COMENTARIOS='" + txt_comentarios.get("1.0", END) +
    #       "' WHERE ID="+ mi_id.get())
    
    # miConexion.commit()
    
    #------------------otra forma de hacerlo-----------------------
    mi_clave_cifrada = mi_passwd.get().encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(mi_clave_cifrada, salt).decode()
    datos =  mi_nombre.get(), hashed, mi_apellido.get(), mi_direccion.get(), txt_comentarios.get("1.0", END)
    miPuntero.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? WHERE ID="+ mi_id.get(), (datos))      
    
    miConexion.commit()
    
    #Columna afectada
    col_afectada = miPuntero.rowcount

    if col_afectada > 0:        
        MessageBox.showinfo("Información", f"El usuario con el id {mi_id.get()} ha sido actualizado correctamente.")
        borrar_campos()
    else:
        MessageBox.showerror("Error", "Algo salió mal con la actualización.")
    
    miConexion.close()
    
#----------------- RAIZ -----------------
raiz = Tk()
#aplicar titulo a la ventana
raiz.title("Ejercicio guiado")

#---------------- VARIABLES DE CLASE --------------------------
#solo para los que son tipo Entry
mi_id = StringVar()
mi_nombre = StringVar()
mi_passwd = StringVar()
mi_apellido = StringVar()
mi_direccion = StringVar()

#----------------- VARIABLES DE BASES DE DATOS ----------------
    
#--------------MENÚ---------------------
menubar = Menu(raiz)
raiz.config(menu=menubar)

screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()
width=300
height=400
# calculate position x and y coordinates
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
raiz.geometry('%dx%d+%d+%d' % (width, height, x, y))

#Una vez creada la barra podemos comenzar a añadir submenús y comandos. 
# Empecemos con los submenús:

bbddmenu = Menu(menubar, tearoff=0)
# Bien ya tenemos nuestra barra con los 3 submenús funcionando bien, 
# pero ocurre algo raro, nos aparece una especie de elemento por defecto. 
# Podemos hacer que desaparezca si indicamos el parámetro tearoff=0:
bbddmenu.add_command(label="Conectar", command=conectar_crear_bbdd)
# Ahora sí que lo tenemos bien, ¿pero está demasiado vacío no? 
# Vamos a añadir comandos de ejemplo en nuestros submenús:
#bbddmenu.add_command(label="Abrir")
#bbddmenu.add_command(label="Guardar")
#bbddmenu.add_command(label="Cerrar")
# También podemos agregar un separador y un comando de salir con raiz.quit:
bbddmenu.add_separator()
bbddmenu.add_command(label="Salir", command=lambda:pregunta_salir())

#Una vez creada la barra podemos comenzar a añadir submenús y comandos. 
# Empecemos con los submenús:

borrarmenu = Menu(menubar, tearoff=0)
borrarmenu.add_command(label="Borrar campos", command=borrar_campos)
#borrarmenu.add_command(label="Copiar")
#borrarmenu.add_command(label="Pegar")

#Una vez creada la barra podemos comenzar a añadir submenús y comandos. 
# Empecemos con los submenús:

crudmenu = Menu(menubar, tearoff=0)
crudmenu.add_command(label="Crear", command=almacenar_informacion)
crudmenu.add_command(label="Leer", command=obtener_datos)
crudmenu.add_command(label="Actualizar", command=actualizar_registro)
crudmenu.add_command(label="Borrar", command=eliminar_registro)
crudmenu.add_separator()
crudmenu.add_command(label="Acerca de...")

#Ya tenemos los submenús, pero todavía nos falta añadirlos a la barra de menú:
menubar.add_cascade(label="BBDD", menu=bbddmenu)
menubar.add_cascade(label="Borrar", menu=borrarmenu)
menubar.add_cascade(label="CRUD", menu=crudmenu)
menubar.add_cascade(label="Ayuda", menu=crudmenu)

#Creamos el frame para incluirlo en la raiz
#--------------FRAME---------------------
mi_frame_1 = Frame(raiz)

mi_frame_1.pack()

#creamos el label
titulo_id = Label(mi_frame_1, text="Id:")
#usaremos grilla para definir la posicion de los elementos dentro de la ventana
#para uusaremos el método grid, para la posicion del elemento
titulo_id.grid(row=0, column=0, sticky=E, padx=10, pady=10)
#titulo_nomre.place(x=100, y=100)

#creamos una caja de texto
#txt_id = Entry(mi_frame_1, state="readonly", textvariable=mi_id)
txt_id = Entry(mi_frame_1, textvariable=mi_id)
#txt_nombre.place(x=100, y=130)
#para uusaremos el método grid, para la posicion del elemento
txt_id.grid(row=0, column=1, sticky=E, padx=10, pady=10)
txt_id.config(justify="center")
#Para la ubicacion de los elementos podemos usar los metodos north, west, south, es decir se usan los puntos cardinales

titulo_nombre = Label(mi_frame_1, text="Nombre:")
titulo_nombre.grid(row=1, column=0,sticky=E, padx=10, pady=10)
txt_nombre = Entry(mi_frame_1, textvariable=mi_nombre)
txt_nombre.grid(row=1, column=1, sticky=E, padx=10, pady=10)
txt_nombre.config(justify="center")


titulo_password = Label(mi_frame_1, text="Password:")
titulo_password.grid(row=2, column=0,sticky=E, padx=10, pady=10)
txt_password = Entry(mi_frame_1, textvariable=mi_passwd)
txt_password.grid(row=2, column=1, sticky=E, padx=10, pady=5)
txt_password.config(justify="center")
#ocultar caracteres de un input
txt_password.config(show='*')

titulo_apellidos = Label(mi_frame_1, text="Apellidos:")
titulo_apellidos.grid(row=3, column=0,sticky=E, padx=10, pady=10)
txt_apellidos = Entry(mi_frame_1, textvariable=mi_apellido)
txt_apellidos.grid(row=3, column=1, sticky=E, padx=10, pady=10)
txt_apellidos.config(justify="center")
#ocultar caracteres de un input


titulo_direccion = Label(mi_frame_1, text="Direccion:")
titulo_direccion.grid(row=4, column=0, sticky=E, padx=10, pady=10)
txt_direccion = Entry(mi_frame_1, textvariable=mi_direccion)
txt_direccion.grid(row=4, column=1, sticky=E, padx=10, pady=10)
txt_direccion.config(justify="center")


titulo_comentarios = Label(mi_frame_1, text="Comentarios:")
titulo_comentarios.grid(row=5, column=0, sticky=E, padx=10, pady=10)
txt_comentarios = Text(mi_frame_1,  height = 5, width = 20)
txt_comentarios.grid(row=5, column=1, sticky=E, padx=10, pady=10)
#Creamos un scroll bar
scrolVertical = Scrollbar(mi_frame_1, command=txt_comentarios.yview)
#posicion dentro de la ventana
#adaptación del scroipbar dentro del txt comentarios
scrolVertical.grid(row=5, column=2,sticky="nsew")
#le ponemos el comportamiento deseado al scroll bar junto con la caja de comentarios
txt_comentarios.config(yscrollcommand=scrolVertical.set, spacing1="7")

#------------------- OTRO FRAME --------------------------
mi_frame_2 = Frame(raiz)
mi_frame_2.pack()

#------------------- Botones ----------------
btn_create = Button(mi_frame_2, text="Create", command=almacenar_informacion)
btn_create.grid(row=1, column=0, sticky="e", padx=10, pady=10)
#btn_create.place(x=25, y=300)

btn_read = Button(mi_frame_2, text="Read", command=obtener_datos)
btn_read.grid(row=1, column=1, sticky="e", padx=10, pady=10)
#btn_read.place(x=90, y=300)

btn_update = Button(mi_frame_2,text="Update", command=actualizar_registro)
btn_update.grid(row=1, column=2, sticky="e", padx=10, pady=10)
#btn_update.place(x=160, y=300)

btn_delete = Button(mi_frame_2,text="Delete", command=eliminar_registro)
btn_delete.grid(row=1, column=3, sticky="e", padx=10, pady=10)
#btn_delete.place(x=250, y=300)

raiz.mainloop()