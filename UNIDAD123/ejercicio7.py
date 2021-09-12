"""EJERCICIO 7.- Realiza un programa que pida dos números 
‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero."""

numero_a=float(input("Ingrese el número a: "))
numero_b=float(input("Ingrese el número b: "))
suma=numero_a+numero_b
signo=""
if(suma>0):
    signo="Positivo"
if(suma<0):
    signo="Negativo"
else:
    signo="Cero"

print(f"La suma de a+b da como resultado :{suma} y es un número {signo}")    


