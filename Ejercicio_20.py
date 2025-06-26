print("Clasificador de triangulos por angulos")
print("el sistema necesita 3 medidas de angulos para estipular que tipo de triangulo es")

Ang1= int(input("Medida primer angulo"))
Ang2= int(input("Medida segundo angulo"))
Ang3= int(input(" Medida Tercer angulo"))
triangulo= Ang1+ Ang2 + Ang3

if triangulo == 180:
    print("Es un triangulo")
    
    if Ang1 == 90 or Ang2 == 90 or Ang3 == 90:
        print ("Es un triangulo rectangulo")
    
    elif Ang1 < 90 and Ang2 < 90 and Ang3 < 90:
        print("Es un triangulo acutangulo")

    elif Ang1 > 90 or Ang2 > 90 or Ang3 > 90:
        print("Es un triangulo obtusangulo")

else: print("No es un triangulo")   