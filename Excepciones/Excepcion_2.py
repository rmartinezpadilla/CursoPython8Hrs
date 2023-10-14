#Manejo de varias excepciones
#de esta manera podemos saber que tipo de erro se está cometiendo
def divide():
    while True: 
        try:        
            numa=(float(input("dame el valor a: ")))
            numb=(float(input("dame el valor b: ")))    
            print ("la division es: " + str(numa/numb))
        
        except ValueError:
            print('Valores incorrectos')
        
        except ZeroDivisionError:
            print('No se puede dividir por cero')

divide()


#Manejo de varias excepciones
#de esta manera NO podemos saber que tipo de erro se está cometiendo
def divide():
    while True: 
        try:        
            numa=(float(input("dame el valor a: ")))
            numb=(float(input("dame el valor b: ")))    
            print ("la division es: " + str(numa/numb))
        
        except ValueError:
            print('An exception occurred')

divide()

