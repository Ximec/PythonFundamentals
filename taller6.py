#TALLER 6 PYTHON
#AUTORA: XIMENA CAMPO LEÓN
#FECHA: 9/5/2023

from datetime import date
hoy = date.today()              #fecha Actual
print("Hoy es el día: " , hoy)
print()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
num1 = int(input("Digite primer número:  "))
print("***Ciclo CONTROLADO POR CONTADOR")
i=1
while i<=num1:
    print(i)
    i+=1
print("fin del ciclo")  

print()
print("ciclo controlado por evento ")
i=1
numero1 = 5
numero2 = int(input("Digite un número del 1 al 10 : "))
while numero2 != numero1:
    i += 1
    numero2 = int(input("Digite un número del 1 al 10 : "))
print(" Acerttaste en el intento No. ", i)
print("Fin del ciclo")

print()
print("*** Ciclo abortado con la sentencia break")
amistad = input("digite el nombre de un amigo: ")
amistad = amistad.upper()
for character in amistad:
    print(character)
    if character ==  "A":
        break
    
print("Fin del ciclo")   

print()
print("FIN")

