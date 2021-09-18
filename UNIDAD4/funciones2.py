import math
"""Ejercicio 1
Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla 
(suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). 
Además subraya el mensaje utilizando el carácter =."""

def escribirCentrado(texto):
   
   longitud=40-(len(texto)//2)
   cadena_final=""
   for i in range(longitud):
       cadena_final+=" "
   cadena_final+=texto    
   print(cadena_final)


"""Ejercicio 2
Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
 Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo."""

def esMultiplo(numero_1,numero_2):
    if numero_1%numero_2==0:
       print(f"El número {numero_1} es múltiplo de {numero_2}")
    if numero_2%numero_1==0:
         print(f"El número {numero_2} es múltiplo de {numero_1}")  

"""Ejercicio 3
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día 
y vaya mostrando la media. El programa pedirá el número de días que se van a introducir."""    
def temperaturaMedia(minima,maxima):
    return (minima+maxima)/2

def temperaturaDias(cantidad_dias):
    dia=1
    temperatura=0
    for i in range(cantidad_dias):
        print(f"Ingrese los datos para el día {dia}")
        dia=dia+1
        minima=float(input("Ingrese la temperatura mínima: "))
        maxima=float(input("Ingrese la temperatura máxima: "))
        temperatura+=temperaturaMedia(minima,maxima)
    print(f"La temperatura media para {cantidad_dias} días es: {temperatura/cantidad_dias}")

"""Ejercicio 4
Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto
 y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, 
 “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función."""

def convertirEspaciado(texto):
    cadena=""
    for i in texto:
        cadena+=" "+i
    print(cadena) 

"""Ejercicio 5
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos
 y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado 
 y muestre el máximo y el mínimo, utilizando la función anterior."""   
def calcularMaxMin(cantidad):
     lista=[]
     contador=1
     for i in range(cantidad):
         numero=int(input(f"Ingrese el {contador} número de la lista: "))
         lista.append(numero)
         contador=contador+1
     print(lista)
     lista.sort()
     min=lista[0]
     max=lista[cantidad-1]
     print(f"El valor mínimo de la lista es: {min} y el valor máximo es {max}")    

"""Ejercicio 6
Diseñar una función que calcule el área y el perímetro de una circunferencia. 
Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.""" 
def perAreaCircunferencia(radio):
    if radio>0:
        area=math.pi*(radio)**2
        perimetro=2*math.pi*radio
        print(f"El área de la circunferencia de radio {radio} es: {area} y su perímetro es: {perimetro}")
    else:
        print("El radio no puede ser un número menor a cero")    

"""Ejercicio 7
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña 
y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
solamente tenemos tres oportunidades para intentarlo."""

def login(usuario,password):
    if usuario=="usuario1" and password=="asdasd" :
       return True
    else:
         return False   

def usuario():
    intentos=0
    while(intentos<3):
        usuario=input("Ingrese el nombre de usuario: ")
        password=input("Ingrese el password: ")
        logeo=login(usuario,password)
        
        if logeo==True:
            print("INGRESO AL SISTEMA CORRECTO!!")
            return
        else:    
         intentos=intentos+1
        
"""Ejercicio 8
Crear una función recursiva que permita calcular el factorial de un número. 
Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial."""    
def factorial(numero): 
    return 1 if (numero==1 or numero==0) else numero * factorial(numero - 1)
             

"""Ejercicio 9
Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:

Se divide el número mayor entre el menor.
Si la división es exacta, el divisor es el MCD.
Si la división no es exacta, dividimos el divisor entre el resto obtenido
 y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD."""

def minimoComun(numero_1,numero_2):
    mcd=0
    mayor=0
    menor=0
    if numero_1>numero_2:
        mayor=numero_1
        menor=numero_2
    else:
        mayor=numero_2
        menor=numero_1
    resto=mayor%menor
    if resto==0:
       mcd=numero_2 
    else:
        mcd=minimoComun(menor,resto)
    return mcd             

"""Ejercicio 10
Escribir dos funciones que permitan calcular:
La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos,
 convertir a horas,minutos y segundos o salir del programa."""
def segundos(horas,minutos,segundos):
      return (horas*3600)+(minutos*60)+segundos

def horas(segundos):
    horas=segundos//3600
    minutos=(segundos%3600)//60
    segundos_3=(segundos%3600)%60
    
    print(f"El número de horas es: {horas} horas con {minutos} minutos y {segundos_3} segundos")


"""Ejercicio 11
El día juliano correspondiente a una fecha es un número entero que indica los días 
que han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal 
que al introducir una fecha nos diga el día juliano que corresponde. 
Para ello podemos hacer las siguientes subrutinas:
LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
EsBisiesto: Recibe un año y nos dice si es bisiesto.
Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano."""
def diaJuliano(anio,mes,dia):
	dia_aux = 0
	for mes in range(1,mes):
		dia_aux = dia_aux + diasMes(mes,anio)
	dia_aux = dia_aux + dia
	return dia_aux

def anioBisiesto(anio):
	return (anio % 4 == 0 and not (anio % 100 == 0)) or anio % 400 == 0

def diasMes(mes,anio):
	if mes in [1,3,5,7,8,10,12]:
		return 31
	elif mes in [4,6,9,11]:
		return 30
	elif mes == 2:
		if anioBisiesto(anio):
			return 29
		else:
			return 28

def leerFecha(anio,mes,dia):
    if dia<0 or dia>diasMes(mes,anio) or mes<0 or mes>12:
        print("Fecha ingresada no válida")
    else: 
        print(f"El correspondiente día juliano de la fecha: {anio}-{mes}-{dia} es el {diaJuliano(anio,mes,dia)}")           


"""Ejercicio 13
Queremos crear un programa que trabaje con fracciones a/b. 
Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.

Vamos a crear las siguientes funciones para trabajar con funciones:

Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. 
Cuando leas una fracción debes simplificarla.
Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
Simplificar_fracción: Esta función simplifica la fracción, 
para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones.
 La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, 
para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. 
Se debe simplificar la fracción resultado.
Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:

Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
Salir"""

def intercambiar(numero_1,numero_2):
	if numero_1<numero_2:
		return numero_2,numero_1
	else:
		return numero_1,numero_2

def calcularMCD(numero_1,numero_2):
	
	numero_1, num2 = intercambiar(numero_1,numero_2)
	resto = numero_1 % numero_2
	if resto == 0: 
		return numero_2
	else:
	  return calcularMCD(numero_2,resto)

def LeerFraccion():
	numerador = int(input("Numerador:"))
	denominador = int(input("Denominador:"))
	numerador,denominador = simplificarFraccion(numerador,denominador)
	return numerador,denominador

def simplificarFraccion(numerador,denominador):
	mcd = calcularMCD(numerador,denominador)
	numerador = numerador / mcd
	denominador = denominador / mcd
	return numerador,denominador

def escribirFraccion(numerador,denominador):
	if denominador!= 1:
		print(str(int(numerador))+"/"+str(int(denominador)))
		
	else:
		print("")
		print(numerador)
		print("")
	
def sumarFracciones(numerador_1,denominador_1,numerador_2,denominador_2):
	numerador = numerador_1*denominador_2 + denominador_1*numerador_2
	denominador = denominador_1 * denominador_2
	numerador,denominador = simplificarFraccion(numerador,denominador)
	return numerador,denominador

def restarFracciones(numerador_1,denominador_1,numerador_2,denominador_2):
	numerador = numerador_1*denominador_2 - denominador_1*numerador_2
	denominador = denominador_1 * denominador_2
	numerador,denominador = simplificarFraccion(numerador,denominador)
	return numerador,denominador

def multiplicarFracciones(numerador_1,denominador_1,numerador_2,denominador_2):
	numerador = numerador_1 * numerador_2
	denominador = denominador_1 * denominador_2
	numerador,denominador = simplificarFraccion(numerador,denominador)
	return numerador,denominador

def dividirFracciones(numerador_1,denominador_1,numerador_2,denominador_2):
	numerador = numerador_1 * denominador_2
	denominador = denominador_1 * numerador_2
	numerador,denominador= simplificarFraccion(numerador,denominador)
	return numerador,denominador

"""MENU PRINCIPAL"""
salir=False
while(salir!=True):  
    print("""*******MENÚ PRINCIPAL CONTROL DE FLUJO Y FUNCIONES UNIDAD 4*******""")
    print("1. CENTRAR TEXTO EJERCICIO 1 FUNCIONES")
    print("2. NÚMEROS MÚLTIPLO EJERCICIO 2 FUNCIONES")
    print("3. TEMPERATURA MEDIA EJERCICIO 3 FUNCIONES")
    print("4. CONVERTIR ESPACIADO TEXTO EJERCICIO 4 FUNCIONES")
    print("5. NÚMERO 0-9 EJERCICIO 5 CONTROL DE FLUJO")
    print("6. LISTAS EJERCICIO 6 CONTROL DE FLUJO")
    print("7. LISTAS ELEMENTOS ÚNICOS EJERCICIO 7 CONTROL DE FLUJO")
    print("8. ÁREA DEL RECTÁNGULO EJERCICIO 8 FUNCIONES")
    print("9. ÁREA DEL CÍRCULO EJERCICIO 2 FUNCIONES")
    print("10. RELACIÓN DE DOS NÚMEROS EJERCICIO 3 FUNCIONES")
    print("11. INTERMEDIO EJERCICIO 4 FUNCIONES")
    print("12. LÍMITES NÚMEROS EJERCICIO 5 FUNCIONES")
    print("13. LISTAS ORDENADAS PARES E IMPARES EJERCICIO 6 FUNCIONES")
    opcion = int(input("Ingrese la opción correspondiente: "))

    if opcion==1:
        print("****CENTRAR TEXTO EJERCICIO 1 FUNCIONES")
        texto=str(input("Ingrese el primer número: "))
        
        escribirCentrado(texto)

    if opcion==2:
        print("****NÚMEROS MÚLTIPLO EJERCICIO 2 FUNCIONES")
        numero_1=int(input("Ingrese el primer número: "))
        numero_2=int(input("Ingrese el segundo número: "))
        esMultiplo(numero_1,numero_2)
    if opcion==3:
        print("****TEMPERATURA MEDIA EJERCICIO 3 FUNCIONES")  
        dias=int(input("Ingrese el número de días: "))
        temperaturaDias(dias)
    if opcion==4:
        print("****CONVERTIR ESPACIADO TEXTO EJERCICIO 4 FUNCIONES") 
        texto=str(input("Ingrese un texto: "))
        convertirEspaciado(texto)
    if opcion==5:
        print("****MÁXIMO Y MÍNIMO DE UNA LISTA EJERCICIO 5 FUNCIONES") 
        cantidad=int(input("Ingrese un número entero(tamaño de la lista): "))
        calcularMaxMin(cantidad)
    if opcion==6:
        print("****DATOS CIRCUNFERENCIA EJERCICIO 6 FUNCIONES") 
        radio=float(input("Ingrese el radio de la circunferencia: "))
        perAreaCircunferencia(radio)  
    if opcion==7:
        print("****LOGIN EJERCICIO 7 CONTROL DE FLUJO") 
        usuario()
    if opcion==8:
        print("****FACTORIAL DE UN NÚMERO EJERCICIO 8 FUNCIONES") 
        numero=int(input("Ingrese el número entero positivo: "))
        print(factorial(numero))

    if opcion==9:
        print("****MCD DE UN NÚMERO EJERCICIO 9 FUNCIONES") 
        numero_1=int(input("Ingrese el primer número: "))
        numero_2=int(input("Ingrese el segundo número: "))
        print(minimoComun(numero_1,numero_2) )
    if opcion==10:
        print("****TIEMPOS EJERCICIO 10 FUNCIONES") 
        salir_1=True
        while(salir_1):
            print("Elija una opción:")
            print("1.- Calcular hora a segundos")
            print("2.-Calcular segundos a horas")
            print("3.- Salir")
            opcion=int(input("Ingrese una opción: "))
            if opcion==1:
                horas_1=int(input("Ingrese las horas: "))
                minutos=int(input("Ingrese los minutos: "))
                segundos_1=int(input("Ingrese los segundos: "))

            if opcion==2:
                segundos_2=int(input("Ingrese los segundos: "))
                horas(segundos_2)
            if opcion==3:
                salir_1=False

    if opcion==11:
        print("****INTERMEDIO EJERCICIO 4 FUNCIONES") 
        anio=int(input("Ingrese el anio: "))
        mes=int(input("Ingrese el mes: "))
        dia=int(input("Ingrese el día: "))
        leerFecha(anio,mes,dia)

        
    if opcion==12:
        print("****LÍMITES NÚMEROS EJERCICIO 5 FUNCIONES") 
        numerador_1=int(input("Ingrese el primer numerador: "))
        denominador_1=int(input("Ingrese el primer denominador: "))
        numerador_2=int(input("Ingrese el segundo numerador: "))
        denominador_2=int(input("Ingrese el segundo denominador: "))

        salir_3=True
        while(salir_3):
            print("***Menú de fracciones***")
            print("1.- Suma de Fracciones")
            print("2.- Resta de Fracciones")
            print("3.- Multiplicación de Fracciones")
            print("4.- División de Fracciones") 
            print("5.- Salir")
            opcion=int(input("Ingrese la opción deseada: "))
            if opcion==1:
                numerador,denominador=sumarFracciones(numerador_1,denominador_2,numerador_2,denominador_2)
                print(f"El resuldado de la suma de las fracciones {numerador_1}/{denominador_1} + {numerador_2}/{denominador_2} es:")
                escribirFraccion(numerador,denominador)
                
                
            if opcion==2:
                numerador,denominador=restarFracciones(numerador_1,denominador_2,numerador_2,denominador_2)
                print(f"El resuldado de la resta de las fracciones {numerador_1}/{denominador_1} - {numerador_2}/{denominador_2} es: {escribirFraccion(numerador,denominador)}")  
            if opcion==3:
                numerador,denominador=multiplicarFracciones(numerador_1,denominador_2,numerador_2,denominador_2)
                print(f"El resuldado de la multiplicación de las fracciones {numerador_1}/{denominador_1} * {numerador_2}/{denominador_2} es: {escribirFraccion(numerador,denominador)}") 
            if opcion==4:
                numerador,denominador=dividirFracciones(numerador_1,denominador_2,numerador_2,denominador_2)
                print(f"El resuldado de la división de las fracciones {numerador_1}/{denominador_1} / {numerador_2}/{denominador_2} es: {escribirFraccion(numerador,denominador)}")   
            if opcion==5:
                salir_3=False                
    
    else:
     salir=False
