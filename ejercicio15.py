"""EJERCICIO 15.- Crea una aplicación que permita adivinar un número. 
En primer lugar la aplicación solicita un número entero por teclado. 
A continuación va pidiendo números y va respondiendo 
si el número a adivinar es mayor o menor que el introducido. 
El programa termina cuando se acierta el número."""
numero=int(input("Ingrese el número: "))
adivina=int(input("Intento adivinar el número ingresado: "))

while(numero!=adivina):
    if(adivina>numero):
        adivina=int(input("El número es mayor al ingresado, ingrese un nuevo número: "))
    else:
        adivina=int(input("El número es menor al ingresado, ingrese un nuevo número: "))

print("Felicitaciones!! Ha Adivinado el número!!")


