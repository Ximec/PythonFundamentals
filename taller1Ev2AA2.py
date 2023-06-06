#TALLER 1 PYTHON
#AUTORA: XIMENA CAMPO LEÓN
#FECHA: 8/5/2023
#Programa para hallar el área de un terreno rectangular

from datetime import date
hoy = date.today()              #fecha Actual
print("Hoy es el día: " , hoy)
base = int(input("Digite la base del terreno:  "))
altura = int(input("Digite la altura del terreno:  "))
area = (base*altura)/2
print("El área del terreno es :  ", area)
print("FIN")