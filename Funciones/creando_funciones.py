#definiendo una función

def mi_funcion():
    print("esto es lo que tiene la función")
    
#llamamos a la función
mi_funcion()

#Creando una función con un parametro
def mi_funcion_2(nombre):
    print(f'esto es lo que tiene la función {nombre}')
    
#llamamos a la función
mi_funcion_2("Juan")

#Creando una función con varios parametros
def mi_funcion_2(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "f":
        print(f'esto es lo que tiene la función querida {nombre} ')
    elif sexo== "m":
        print(f'esto es lo que tiene la función querido {nombre} ')
    else:
        print("no eres ni hombre ni mujer locota")
    
#llamamos a la función
mi_funcion_2("Ana", "F")

#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
#desempaquetando la funciòn
password,primer_numero = crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El nùmero utilizado para crearla fue: {primer_numero}")