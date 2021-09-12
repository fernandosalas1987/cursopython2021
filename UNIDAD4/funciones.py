import math

"""1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta."""
def operaciones(a,b):
   salir=False
   while(salir!=True):  
    print("""*******MENÚ EJERCICIO 1 FUNCIONES UNIDAD 4*******""")   
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Opcion 3")
    print("4. Salir")
    opcion = int(input("Ingrese la opción correspondiente: "))
    if opcion==1:
        print(f"La suma de los dos números es: {a+b}")
    if opcion==2:
        print(f"La suma de los dos números es: {a-b}")
    if opcion==3:
        print(f"La suma de los dos números es: {a-b}") 
    else:
        print("Ha ingresado una opción incorrecta!")
        salir=True    

""" 2) Realiza un programa que lea un número impar por teclado.
 Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente."""
def numero_Impar(numero):
     
     while numero % 2 == 0: 
        numero = int(input(f"El número {numero} no es un número impar. Inténtelo de nuevo! ") )

"""3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. 
El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo."""
def numeros_pares():
    resultado=sum(range(0,101,2))
    print(resultado)

"""4) Realiza un programa que pida al usuario cuantos números quiere introducir. 
Luego lee todos los números y realiza una media aritmética:"""
def media_Aritmetica(cantidad_numeros):
    suma=0
    
    for num in range(cantidad_numeros):
        numero=float(input("Ingrese los números: "))
        suma+=numero
    print(f"La media aritmética es la siguiente: {suma/cantidad_numeros} para la suma {suma}")    

"""5) Realiza un programa que pida al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor 
se encuentra en una lista (devuelve True o False)"""
def numeros_cero_nueve(numero):
    while numero < 0 or numero > 9: 
        if numero <0 or numero > 9: 
            numero = float(input(f"El número {numero} no está entre 0 y 9. Inténtelo de nuevo! ") )
         
    if(numero>=0 and numero<=9):
        print(f"El número {numero} está entre 0 y 9!!")    
         
"""6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
Pista: Utiliza el tercer parámetro de la función range(inicio, fin, salto). """
def listas():
    print(f"Lista 0-10: {list(range(0,11))}")
    print(f"Lista -10-0: {list(range(-10,1))}")
    print(f"Lista pares 0-20: {list(range(0,21,2))}")
    print(f"Lista impares -20-1: {list(range(-19,0,2))}")
    print(f"Lista múltiplos de 5 0-50: {list(range(0,51,5))}")

"""7) Dadas dos listas, debes generar una tercera con todos los elementos 
que se repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:
"""
def elementosUnicos():
    lista_1=[1,2,3,4,5,7,9]
    lista_2=[2,5,7,9]
    lista_final=[]

    for numero in lista_1:
        if numero in lista_2 and numero not in lista_final:
            lista_final.append(numero)
    print(lista_final)        

"""Funciones (Enunciados)"""
"""1) Realiza una función llamada area_rectangulo() que devuelva el área del rectangulo 
a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura.
Nota: El área de un rectángulo se obtiene al multiplicar la base por la altura."""

def area_Rectangulo(base,altura):
       if base>0 and altura>0:
        print(f"El área del rectángulo de base 15 y altura 10 es de {base*altura} unidades cuadradas")
       else:
           print("La base y altura deben ser números positivos, imposible cálcular el área")


"""2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
Calcula el área de un círculo de 5 de radio;
Nota: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi.
 Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:"""
def area_circulo(radio):
     if radio>0:
      print(f"El área del círculo de radio {radio} es: {math.pi*(radio**2)}")
     else:
         print("Error!! El radio no puede ser un número negativo") 

"""3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.
Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'"""

def relacion(a,b):
    if a>b:
        return 1
    if a<b:
        return -1
    return 0    



"""4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

Nota: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

Comprueba el punto intermedio entre -12 y 24"""
def intermedio(a,b):
    print(f"El punto intermedio entre {a} y {b} es: {(a+b)/2}")

"""5) Realiza una función llamada recortar() que reciba tres parámetros.
 El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. 
 La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste
Devolver el límite superior si el número es mayor que éste.
Devolver el número sin cambios si no se supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10"""

def recortar(recortar,lim_inf,lim_sup):
    if lim_inf>lim_sup:
        print(f"El límite inferior {lim_inf} supera al límite superior {lim_sup}")
    if recortar<lim_inf :
        print(f"Límite inferior: {lim_inf}")
    if recortar>lim_sup :
        print(f"Límite superior: {lim_sup}")
    if recortar>=lim_inf and recortar<=lim_sup:
        print(f"El número {recortar} no supera los límites inferior y superior")  

"""6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, y la segunda con los números impares:"""
def listas_ordenadas():
    lista_original=[10,2,3,9,4,6,7,8,5,1]
    lista_pares=[]
    lista_impares=[]
    for i in lista_original:
        if i%2==0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)

    lista_pares.sort()
    lista_impares.sort()        
    print(f"Lista original: {lista_original}")
    print(f"Lista pares: {lista_pares}")
    print(f"Lista impares: {lista_impares}")        




"""MENU PRINCIPAL"""
salir=False
while(salir!=True):  
    print("""*******MENÚ PRINCIPAL CONTROL DE FLUJO Y FUNCIONES UNIDAD 4*******""")
    print("1. OPERACIONES DOS NÚMEROS EJERCICIO 1 CONTROL DE FLUJOS")
    print("2. NÚMERO IMPAR EJERCICIO 2 CONTROL DE FLUJO")
    print("3. IMPRIMIR PARES DE 0 A 100 EJERCICIO 3 CONTROL DE FLUJO")
    print("4. MEDIA ARITMÉTICA EJERCICIO 4 CONTROL DE FLUJO")
    print("5. NÚMERO 0-9 EJERCICIO 5 CONTROL DE FLUJO")
    print("6. LISTAS EJERCICIO 6 CONTROL DE FLUJO")
    print("7. LISTAS ELEMENTOS ÚNICOS EJERCICIO 7 CONTROL DE FLUJO")
    print("8. ÁREA DEL RECTÁNGULO EJERCICIO 1 FUNCIONES")
    print("9. ÁREA DEL CÍRCULO EJERCICIO 2 FUNCIONES")
    print("10. RELACIÓN DE DOS NÚMEROS EJERCICIO 3 FUNCIONES")
    print("11. INTERMEDIO EJERCICIO 4 FUNCIONES")
    print("12. LÍMITES NÚMEROS EJERCICIO 5 FUNCIONES")
    print("13. LISTAS ORDENADAS PARES E IMPARES EJERCICIO 6 FUNCIONES")
    opcion = int(input("Ingrese la opción correspondiente: "))

    if opcion==1:
        print("Ingrese dos números: ")
        numero_1=float(input("Ingrese el primer número: "))
        numero_2=float(input("Ingrese el segundo número: "))
        operaciones(numero_1,numero_2)

    if opcion==2:
        print("****NÚMERO IMPAR EJERCICIO 2 CONTROL DE FLUJO")
        numero=int(input("Ingrese un número entero: "))
        numero_Impar(numero)
    if opcion==3:
        print("****IMPRIMIR PARES DE 0 A 100 EJERCICIO 3 CONTROL DE FLUJO")  
        numeros_pares()
    if opcion==4:
        print("****MEDIA ARITMÉTICA EJERCICIO 4 CONTROL DE FLUJO") 
        cantidad=int(input("Introduce la cantidad de números que desea ingresar: "))
        media_Aritmetica(cantidad)
    if opcion==5:
        print("****NÚMERO 0-9 EJERCICIO 5 CONTROL DE FLUJO") 
        entero=int(input("Ingrese un número entero: "))
        numeros_cero_nueve(entero) 
    if opcion==6:
        print("****LISTAS EJERCICIO 6 CONTROL DE FLUJO") 
        listas()  
    if opcion==7:
        print("****LISTAS ELEMENTOS ÚNICOS EJERCICIO 7 CONTROL DE FLUJO") 
        elementosUnicos() 
    if opcion==8:
        print("****ÁREA DEL RECTÁNGULO EJERCICIO 1 FUNCIONES") 
        base=float(input("Ingrese la base del rectángulo: "))
        altura=float(input("Ingrese la altura del rectángulo: "))
        area_Rectangulo(base,altura) 

    if opcion==9:
        print("****ÁREA DEL CÍRCULO EJERCICIO 2 FUNCIONES") 
        radio=float(input("Ingrese el radio del círculo: "))
        area_circulo(radio)  
    if opcion==10:
        print("****RELACIÓN DE DOS NÚMEROS EJERCICIO 3 FUNCIONES") 
        numero_1=float(input("Ingrese el primer número: "))
        numero_2=float(input("Ingrese el segundo número: "))
        print(relacion(numero_1,numero_2) ) 

    if opcion==11:
        print("****INTERMEDIO EJERCICIO 4 FUNCIONES") 
        numero_1=float(input("Ingrese el primer número: "))
        numero_2=float(input("Ingrese el segundo número: "))
        intermedio(numero_1,numero_2)  

    if opcion==12:
        print("****LÍMITES NÚMEROS EJERCICIO 5 FUNCIONES") 
        recortar_num=float(input("Ingrese el número a recortar: "))
        lim_inf=float(input("Ingrese el límite inferior: "))
        lim_sup=float(input("Ingrese el límite superior: "))
        recortar(recortar_num,lim_inf,lim_sup)     
    if opcion==13:
        print("LISTAS ORDENADAS PARES E IMPARES EJERCICIO 6 FUNCIONES")
        listas_ordenadas()
    else:
     salir=True



    


            
       

