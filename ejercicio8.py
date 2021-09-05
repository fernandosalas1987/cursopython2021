#EJERCICIO 8.-  Escribe un programa que lea un número e indique si es par o impar.
numero=int(input("Ingrese el número: "))
if numero%2==0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")