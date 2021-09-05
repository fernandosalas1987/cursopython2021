"""EJERCICIO 9.-  Escribe un programa que pida un número entero 
entre uno y doce e imprima el número de días que tiene el mes correspondiente."""
numero_mes=int(input("Ingrese un número entero entre uno y doce : "))
if numero_mes>0 and numero_mes<13:
    if numero_mes==1 or numero_mes==12 or numero_mes==7 or numero_mes==10 or numero_mes==5 or numero_mes==8 or numero_mes==3:
        print(f"El mes {numero_mes} tiene 31 días")
    if numero_mes==4 or numero_mes==6 or numero_mes==9 or numero_mes==11:
         print(f"El mes {numero_mes} tiene 30 días")
    if numero_mes==2:
        print(f"El mes {numero_mes} tiene 28 días")
else:
    print("Número no válido, vuelva a ejecutar el programa!!")
   