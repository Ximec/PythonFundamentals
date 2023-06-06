#TALLER 4 PYTHON
#AUTORA: XIMENA CAMPO LEÓN
#FECHA: 8/5/2023

from datetime import date
hoy = date.today()              #fecha Actual
print("Hoy es el día: " , hoy)
print()
print("ADIVINA UN ANIMAL")
pelo = input("¿Tiene Pelo?, responde s para si o n para no: ")
if pelo == "s":
    print("El animal es un mamífero")
else:
    plumas =input("¿Tiene plumas?, responde s para si o n para no: ")
    if plumas == "s":
        print("El animal es un ave")
    else:
        escamas  = input("¿Tiene escamas?, responde s para si o n para no: ")
        if escamas == "s":
            print("El animal es un pez")   
        else:
            print("el animal No está dentro de las 3 categorias que hemos selecconado")
print()
print("FIN")

