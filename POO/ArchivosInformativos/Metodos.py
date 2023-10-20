class Celular():
    llamando = False
    #Método constructor de la clase
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        llamando = True
        return llamando
    
    def colgar(self):
        llamando = False
        return llamando
#objeto
mi_telefono_a = Celular("TCL", "65' pulgadas", "48MPX")
mi_telefono_b = Celular("Samsumg", "S 10", "48MPX")

#print(mi_telefono_a.marca)

if mi_telefono_a.llamar() == True:
  print("acabas de iniciar una llamada")
finalizar = input("presiona 'x' para colgar la llamada: ")  
while finalizar != "x":    
    finalizar = input("presiona 'x' para colgar la llamada: ") 
    if finalizar == "x":
       mi_telefono_a.colgar()
       print("haz colgado la llamada desde tu telefono")

    

    
    


#print(mi_telefono_b.marca)