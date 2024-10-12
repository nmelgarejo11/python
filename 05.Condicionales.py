# Verificar si un número es positivo, negativo o cero
numero_validar = 0
if (numero_validar == 0):
    print("valor en cero")
elif (numero_validar < 0):
    print("valor es negativo")
else:
    print("valor es positivo") 
    
# Determinar si un estudiante aprobó o no
nota_estudiante: 50
calificasion_aprobo: 60
if (nota_estudiante >= calificasion_aprobo):
    print("estudiante aprobo")
else:
    print("estudiante no aprobo")

# Comprobar si un número es par o impar
verificar_numero: 45
if (verificar_numero % 2 == 0):
    print("el numero" + str(verificar_numero) +  " es par")
else:
    print("el numero" + str(verificar_numero) + " no es par")

# Verificar si un número está dentro de un rango
numero_rango: 3
if (numero_rango in (1, 10)):
    print("en el rango")
else:
    print("no esta en el rango")