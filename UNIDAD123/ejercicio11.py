"""EJERCICIO 11.-Escribir un programa que lea un año indicar si es bisiesto. 
Nota: un año es bisiesto si es un número divisible por 4, 
pero no si es divisible por 100, excepto que también sea divisible por 400."""
anio=int(input("Ingrese el año: "))
if anio%4==0 or anio%400==0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")    