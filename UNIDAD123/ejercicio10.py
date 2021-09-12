"""EJERCICIO 10.- Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “passwd#” 
se indica “Has entrado al sistema”, sino se da un error."""
usuario=str(input("Ingrese el nombre de usuario: "))
password=str(input("Ingrese la contraseña : "))
if usuario=="pepe" and password=="passwd#":
    print("Has entrado al sistema!!")
else:
    print("Error!!")    