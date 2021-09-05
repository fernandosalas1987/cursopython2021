#EJERCICIO 13.- Pedir un número por teclado y mostrar la tabla de multiplicar
numero=int(input("Ingrese el número: "))
print(f"La tabla de multiplicar del número {numero} es la siguiente: ")
contador=1;
while contador<=100:
    tabla=contador*numero
    print(f"{contador} x {numero} = {tabla}")
    contador=contador+1

