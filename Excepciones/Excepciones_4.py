import math

def calculaRaiz(num):
    if num < 0:
        raise ValueError("El número no puede ser negativo...")
    else:
        return math.sqrt(num)

dato = (int(input("Dame el valor por favor: ")))

try:
    print(calculaRaiz(dato))
except ValueError as ErrorPersonalizado:
    print(ErrorPersonalizado)

print("terminando...")