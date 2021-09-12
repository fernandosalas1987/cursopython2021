#EJERCICIO 3.- Dados dos números, mostrar la suma, resta, división y multiplicación de ambos
numero_a=float(input("Ingrese el primer número: "))
numero_b=float(input("Ingrese el segundo número: "))



suma=numero_a+numero_b
resta=numero_a-numero_b
multiplicacion=numero_a*numero_b
if numero_b==0:
    division=0
else:
    division=numero_a/numero_b

print(f"El resultado de la suma es {suma}")
print(f"El resultado de la resta es {resta}")
print(f"El resultado de la multiplicación es {multiplicacion}")
print(f"El resultado de la división es {division}")
