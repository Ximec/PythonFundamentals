#TALLER 2 PYTHON
#AUTORA: XIMENA CAMPO LEÓN
#FECHA: 8/5/2023

from datetime import date
hoy = date.today()              #fecha Actual
print("Hoy es el día: " , hoy)
a = int(input("Digite el primer número:  "))
b = int(input("Digite el segundo número:  "))
c = int(input("Digite el tercer número:  "))
d = int(input("Digite el cuarto número:  "))
x = [a, b, c, d]
print(x)
print("El valor máximo es: ", max(x))
print("El valor mínimo es: ", min(x))
print("El tamano del la lista es: ", len(x))
print("La lista revertida es: ", list(reversed(x)))
print()
frase = input("Digite una oración: ")
print("la frase dividida en palabras es: ", frase.split())
print("La frase en mayúscula es: ", frase.upper())
print("La frase con mayúscula inicial es: ", frase.capitalize())
frase2 = input("Digite una nueva oración: ")
print("La frase : " + frase + " se reemplazo por: "+ frase.replace(frase,frase2))
print()
print("FIN")

