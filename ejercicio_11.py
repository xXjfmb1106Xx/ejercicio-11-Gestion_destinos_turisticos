print("EJERCICIO 11: GESTION DE DESTINOS TURISTICOS \n")

print("NOMBRES VIAJEROS\n")
v1= input("ingrese nombre del viajero numero 1 ")
v2= input("ingrese nombre del viajero numero 2 ")
v3= input("ingrese nombre del viajero numero 3 ")
print(f"el nombre de los viajeros es {v1},{v2} y {v3}")

print("DESTINOS TURISTICOS\n")
d1= input("ingrese nombre del destino numero 1 ")
d2= input("ingrese nombre del destino numeroS 2 ")
d3= input("ingrese nombre del destino numero 3 ")
print(f"los destinos turisticos buscados son {d1},{d2} y {d3}")

viajeros= [v1.capitalize(),v2.capitalize(),v3.capitalize()]
destinos= [d1.capitalize(),d2.capitalize(),d3.capitalize()]

#1
if "Valeria" in viajeros:
    viajeros.append("Santiago")
    print(viajeros)
#2  
elif "San Andres" in destinos:
    destinos.append("Santa Marta")
    print(destinos)
#3
elif "Tomas" in viajeros:
    viajeros.remove("Tomas")
    print(viajeros)
#4
elif len(destinos) > 3:
    destinos.remove(0)
    print(viajeros)
#5
elif "Daniela" in viajeros:
    viajeros.remove("Daniela")
    viajeros.append("Julieta")
    print(viajeros)
#6
print("GRUPO 1")
grupo1= [viajeros[0],viajeros[1]]
print(grupo1)
#7
print("COSTEÑOS")
costeños = [destinos[-1],destinos[-2]]
print(costeños)
#8
if "Santa Marta" in costeños:
    playa_destacada=("Santa Marta",4.7)
    print(playa_destacada)
#9
elif "Julieta" in grupo1:
    grupo1.append("Check-in listo")
    print(grupo1)
#10
elif "Check-In Listo" in grupo1:
    reserva={
        "nombre" : "Julieta",
        "destino" : "Medellin",
        "confirmado": True
        }
    print(f"informacion de la reserva {reserva}")
#11    
    if reserva in globals():
        reserva["vuelo"]= "V-2345"
        print(f"registro terminado, informacion completa de la reserva: {reserva}")
#12
elif not "Bogota" in destinos:
    destinos.append("Bogota")
    print(viajeros)
#13
elif not "Tomas" in viajeros:
    viajeros.append("Tomas")
    print(viajeros)
        
print(" RESULTADOS DEL REGISTRO \n")

print("viajeros",viajeros)
print("destinos",destinos)
print("grupo 1",grupo1)
print("costeños",costeños)
