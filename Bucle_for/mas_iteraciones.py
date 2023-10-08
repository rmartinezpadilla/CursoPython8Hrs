mis_verduras = ["cebolla roja", "cebolla blanca", "pimenton", "ají topito", "calabaza"]
mi_cadena_de_texto = "esto es una gran cadena de texto"
numeros = [2, 6, 9, 7, 6]

#evitando que se coma una fruta usando al sentencia "continue"
for verdura in mis_verduras:
    if verdura == 'pimenton':
        continue
    print(f'Me voy a comer {verdura}')
    
#evitando que el ciclo continúe al momento de seleccionar una verdura no deseada
for verdura in mis_verduras:
    if verdura == 'pimenton':
        break
    print(f'Me voy a comer {verdura}')
    
#iterar cadenas de texto
for letra in mi_cadena_de_texto:
    print(letra)
    
#llenando otra lista
numeros_multiplicados = [x*2 for x in numeros]
print(numeros_multiplicados)