#creando conjuntos con la función set()

mi_conjunto = set(["dato 1", "dato 2", "dato 3"])
print(mi_conjunto)

# Usando la función frocenset() para meter un conjunto dentro de otro conjunto
conjunto_1 = frozenset(["dato 1", "dato 2"])
conjunto_2 = {conjunto_1, "dato 3"}

print(conjunto_2)

#validamos si un conjunto es SUBCONJUNTO de otro conjunto con el método issubset()
#creamos dos conjuntos
conjunto_a={2, 4, 6, 8, 10, 12, 14}
conjunto_b={2, 6, 8, 12}

#forma de verificar usando el método
resultado_1 = conjunto_b.issubset(conjunto_a)

#forma de verificar usando el menor o igual
#resultado = conjunto_b <= conjunto_a

if resultado_1:
  print("el conjunto b es subconjunto del conjunto a")
else:
  print("el conjunto b no es subconjunto del conjunto a")


#validamos si un conjunto es un SUPERCONJUNTO de otro conjunto con el método issuperset()
#creamos dos conjuntos
conjunto_a={2, 4, 6, 8, 10, 12, 14}
conjunto_b={2, 6, 8, 12}

#forma de verificar usando el método
resultado_2 = conjunto_b.issuperset(conjunto_a)

#forma de verificar usando el menor o igual
#resultado = conjunto_b < conjunto_a

if resultado_2:
  print("el conjunto b es superconjunto del conjunto a")
else:
  print("el conjunto b no es superconjunto del conjunto a")
  
# validamos que un conjunto sea distinto de otro
#con que un valor de uno de los conjutos sea igual el método devolerá false
resultado_3= conjunto_a.isdisjoint(conjunto_b)
if resultado_3==False:
  print("el conjunto b tiene al menos un valor del conjunto a")
else:
  print("el conjunto b No tiene ningún valor del conjunto a")