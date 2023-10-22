class Tanque():
    def __init__(self):
        self.__litros = 0
    
    @property
    def combustible(self):
        return self.__litros
    
    @combustible.setter
    def combustible(self, litros):
        self.__litros = litros
        
    def usar_combustible(self, litro):
        self.__litros -= litro

class Auto():
    def __init__(self, tanque):
        self.__posicion = 0
        self.__combustible = tanque
    
    def mover(self, distancia):
        if self.__combustible.combustible >= distancia / 2:
            self.__posicion += distancia
            self.__combustible.usar_combustible(distancia / 2)
            print ("se ha modivo correctamente")
        else:
            print ('No hay combustible')
    
    @property
    def posicion(self):
        return self.__posicion
    
    @posicion.setter
    def posicion(self, metros):
        self.__posicion += metros
    
    @property
    def combustible(self):
        return self.__combustible
    
    @combustible.setter
    def combustible(self, litros):
        self.__combustible += litros


mi_tanque = Tanque()
mi_tanque.combustible = 100

my_car = Auto(mi_tanque)


print(my_car.posicion)
my_car.mover(10)
print('Combustible actual: ', mi_tanque.combustible)
print(my_car.posicion)
my_car.mover(20)
print('Combustible actual: ', mi_tanque.combustible)
print(my_car.posicion)
my_car.mover(60)
print('Combustible actual: ', mi_tanque.combustible)
print(my_car.posicion)
my_car.mover(80)
print('Combustible actual: ', mi_tanque.combustible)
print(my_car.posicion)
my_car.mover(100)
print('Combustible actual: ', mi_tanque.combustible)
print(my_car.posicion)
my_car.mover(120)
print('Combustible actual: ', mi_tanque.combustible)
print(my_car.posicion)

# r9 = Auto()
# r9.posicion = 0
# r9.combustible = 100 

# r9.mover(20)
# print(f'La posicion actual es: {r9.posicion}, y el combustible que tiene es de: {r9.combustible} litros')
# r9.mover(30)
# print(f'La posicion actual es: {r9.posicion}, y el combustible que tiene es de: {r9.combustible} litros')
# r9.mover(40)
# print(f'La posicion actual es: {r9.posicion}, y el combustible que tiene es de: {r9.combustible} litros')
# r9.mover(50)
# print(f'La posicion actual es: {r9.posicion}, y el combustible que tiene es de: {r9.combustible} litros')
# r9.mover(60)
# print(f'La posicion actual es: {r9.posicion}, y el combustible que tiene es de: {r9.combustible} litros')
# r9.mover(70)
# print(f'La posicion actual es: {r9.posicion}, y el combustible que tiene es de: {r9.combustible} litros')