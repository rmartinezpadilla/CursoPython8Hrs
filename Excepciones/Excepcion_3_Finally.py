#Manejo de varias excepciones
# Cuando no controlamos ninguna excepcion pero queremos que al final siempre se ejecute algo
# usamos las senencia finally

def divide():
    
        try:        
            numa=(float(input("dame el valor a: ")))
            numb=(float(input("dame el valor b: ")))    
            print ("la division es: " + str(numa/numb))
        #comentamos al excepcion por que no queremos controlarla
        #except ValueError:
        #a su vez usamos el metodo finally
        finally:
            print('Calculo finalizado')

divide()