#TALLER 6 PYTHON
#AUTORA: XIMENA CAMPO LEÓN
#FECHA: 9/5/2023

from datetime import date
hoy = date.today()              #fecha Actual
print("Hoy es el día: " , hoy)
print()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()

print("NÚMERO PRIMO")
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

print("COMPROBAR CONTRASEÑA")

password_1 = input("Escriba su contraseña: ")
password_2 = input("Escriba de nuevo su contraseña: ")
while password_1 != password_2:
        print("Las contraseñas no coinciden. Inténtelo de nuevo.")
        password_1 = input("Escriba su contraseña: ")
        password_2 = input("Escriba de nuevo su contraseña: ")
print("Contraseña confirmada")        


print()
print("*** Ciclo abortado con la sentencia break")
pregunta = input("¿Desea continuar  programa?, escriba s para si o n para no: ")
pregunta = pregunta.upper()
for character in pregunta:
    print(character)
    if character ==  "N":
        print("sale del programa")
        break
    if character ==  "S":
        print("sigue  programa")
        break

print("Fin del ciclo")   

print()
print("FIN")

