#generando numeros pares de manera tradicional
def generaNumerosPares(limite):
    numero = 1
    miLista=[]
    
    while numero <= limite:
        miLista.append(numero*2)
        numero+=1
    
    return miLista

print(generaNumerosPares(2))

#generando numeros pares de manera optima con yield

def generaPares(limite):
    numero = 1    
    
    while numero < limite:
        yield numero * 2         
        numero+=1
    
print(generaNumerosPares(10))

#generando numeros pares de manera optima con yield
# pero en este caso lo podemos controlar

def generaPares(limite):
    numero = 1    
    
    while numero < limite:
        yield numero * 2         

        numero+=1

misPares = generaPares(10)

print(next(misPares))
print("Leyendo el siguiente...")
print(next(misPares))
print("Leyendo el siguiente...")
print(next(misPares))
print("Leyendo el siguiente...")