#funciones lambda
# por lo general se usan en funciones sencillas
#lo que haces es simplificar un poco la funcion
#funciones anonimas, funcones on the go, on demand, online

area_triangulo=lambda base, altura:(base*altura)/2

print(area_triangulo(7, 5))


#Otro ejemplo


al_cubo=lambda numero:pow(numero, 3)

print(al_cubo(23), type(al_cubo))