#TALLER 5 PYTHON
#AUTORA: XIMENA CAMPO LEÓN
#FECHA: 8/5/2023

from datetime import date
hoy = date.today()              #fecha Actual
print("Hoy es el día: " , hoy)
print()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()
num1 = int(input("Digite primer número:  "))
num2 = int(input("Digite segundo número:  "))
print("Ciclo para imprimir desde el 1 en cuenta progresiva")
for i in range(1,num1):
    print(i)
print("fin del ciclo")  

print()
print("ciclo cuenta regresiva ")
for i in range(1,num2+1):
     print("     ",num2-i)
print("Fin del ciclo") 

print()
nombre = input("Digite su nombre: ")
nombre = nombre.title()
for character in nombre:
    print(character)
print("Fin del ciclo")    

print()
print("FIN")

