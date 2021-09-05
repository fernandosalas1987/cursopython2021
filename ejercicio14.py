"""EJERCICIO 14.- Crea una aplicación que pida un número y 
calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número 
y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120"""

numero=int(input("Ingrese el número: "))
contador=1
factorial=1
while contador<=numero:
    factorial*=contador
    contador=contador+1
print(f"el factorial de {numero} es: {factorial}")    