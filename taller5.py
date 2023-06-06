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
print("Ciclo para el primer número")
for i in range(num1):
    print(i)
print("fin del ciclo")  

print()
print("ciclo desde e promer número hasta el segundo número")
for i in range(num1, num2):
    print(i)
print("Fin del ciclo") 

print()
print("Ciclo desde el primero hasta el segundo numero con incrementos de 2")
for i in range(num1, num2, 2):
    print(i)
print("Fin del ciclo") 

print()
empresa = input("Digite nombre de una empresa: ")
empresa = empresa.lower()
for character in empresa:
    print(character)
print("Fin del ciclo")    

print()
print("FIN")

