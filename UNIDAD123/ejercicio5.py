"""EJERCICIO 5.-Realiza un programa que reciba una cantidad 
de minutos y muestre por pantalla a cuantas horas y minutos corresponde."""
minutos=float(input("Ingrese el número de minutos: "))
horas=minutos//60
minutos_1=minutos%60
print(f"El número de horas es: {horas} con {minutos_1} minutos")

