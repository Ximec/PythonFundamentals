#TALLER 2 PYTHON
#AUTORA: XIMENA CAMPO LEÓN
#FECHA: 8/5/2023

from datetime import date
hoy = date.today()              #fecha Actual
print("Hoy es el día: " , hoy)
a = int(input("Digite su edad:  "))
b = int(input("Digite la edad de su amigo:  "))
if a >= b:
    print("usted es mayor que su amigo")
else:
    print("su amigo es mayor que usted")    
print()    
compra1 = "manzanas"
compra2= "peras"
print("la fruta 1 es : ", compra1)
print("la fruta 2 es : ", compra2)
if compra1 == "manzanas" and compra2 =="peras":
    print("usted compró frutas ")
else:
    print("usted compró verduras")    
print()    
print("*** Final del analisis del programa compras en almacen")
print()
frase = input("Digite una oración: ")
print("La frase con mayúscula inicial es: ", frase.capitalize())
print("la frase dividida en palabras es: ", frase.split())
x=frase.split()
longitud = len(x)
print("la frase tiene :  " , len(x),  "palabras")
if longitud < 5:
    print("El número de palabras que contiene la frase es menor a 5 , esta frase contiene", len(x))
else:
    print("El número de palabras que contiene la frase es mayor o igual  5 , esta frase contiene", len(x))
print()
print("FIN")

