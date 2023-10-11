divisas = {
    'Euro':'€', 
    'Dollar':'$', 
    'Yen':'¥'
}

#otra forma de acceder al valor de una llave dentro de un diccionario
print(divisas.get("Euro".title()))

def visualizarDivisa(divisa):
    resultado = f"la divisa {divisa} no existe"
    for datos in divisas.items():
        key = datos[0]    
        if key==divisa:         
          resultado=datos[1]        
    
    return resultado        


seleccion = input("Hola, que divisa quieres ver? ")

print(visualizarDivisa(seleccion))


#solución II
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")