#para poder trabajar con ficheros importamos la librería pickle
import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.gerenero = genero
        self.edad = edad
        print (f'se ha creado una persona con el nombre {self.nombre}')
    
    #metodo nuevo no lo conozco vamos a ver que tal funciona
    def __str__(self):
        return "{} {} {} ".format(self.nombre, self.gerenero, self.edad)

class ListaPersonas:
    
    personas = []
    
    #creamos un constructor para que los datos se guardenb automaticamente en un archivo
    def __init__(self) -> None:
        #el fichero lo crea en la raiz del proyecto
        listaDePersonas = open("ficheroExterno", "ab+")
        #mover el curso a la primera posicion del archivo
        listaDePersonas.seek(0)
        #llamamos la lista que ya tenemos llena usando el metodo agregar persona
        # Usamos un try catch por si el fichero está vacio o no puede realizar la operacion pueda tomar otra ruta
        try:
            self.personas = pickle.load(listaDePersonas)
            print("se cargaron {} personas al fichero externo".format(len(self.personas)))        
        except:
            print("el fichero está vacío")
            
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
            
    #creamos un metodo para guardar personas en el fichero externo
    def guardar_persona_en_fichero(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    
    def mostrar_info_de_fichero_externo(self):
        print("la informacion del fichero externo es:")
        for p in self.personas:
            print (p)
    
    def agregar_persona(self, persona):
        self.personas.append(persona)
        #aqui llamamos al método para poder guardar la persona en el fichero
        self.guardar_persona_en_fichero()
    
    def mostrar_personas(self):
        for p in self.personas:
            print(p)
    
    
            
#creamos una instancia de la clase listapersonas para poder usar los métodos de la clase

# mi_lista = ListaPersonas()
# p = Persona("Rubén", "M", 23)
# mi_lista.agregar_persona(p)
# p = Persona("Ana", "F", 33)
# mi_lista.agregar_persona(p)
# p = Persona("Lisa", "F", 52)
# mi_lista.agregar_persona(p)
# p = Persona("marlon", "M", 19)
# mi_lista.agregar_persona(p)

# mi_lista.mostrar_personas()

            
#creamos una instancia de la clase listapersonas para poder usar los métodos de la clase
mi_lista = ListaPersonas()
# instanciamos la clase persona para crear una persona
p = Persona("Rubén", "M", 23)
#usamos el metodo agregar persona y hace todo eso que tiene dicho el módulo
mi_lista.agregar_persona(p)
# instanciamos la clase persona para crear una persona
p = Persona("Ana", "F", 65)
#usamos el metodo agregar persona y hace todo eso que tiene dicho el módulo
mi_lista.agregar_persona(p)

#mostramos la informacion que tiene el fichero
mi_lista.mostrar_info_de_fichero_externo()