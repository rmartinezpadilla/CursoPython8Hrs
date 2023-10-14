#validar que tipo de calificacion obtiene un estudiante dependiendo su nota

def calificacion(nota):
    if nota < 5:
        return "insuficiente"
    elif nota < 7:
        return "suficiente"
    elif nota < 9:
        return "muy bien"
    else:
        return "excelente"
    

print(calificacion(8))