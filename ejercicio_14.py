print("IDENTIFICADOR DE FECHA PALINDROMA")
print("""Una fecha palindroma es una fecha la cual""")
print("""se lee igual de izquierda a derecha y de derecha a izquierda
     ejemplo:  22/02/2022 (D/M/A)""")  # definicion

dia = int(input("escribe el dia "))  #variable de dia  
mes = int(input("escribe el mes "))  #variable de mes
year= int(input("escribe el año ")) #variable de año
fecha= (f"{dia:02d}{mes:02d}{year:04d}") # {dia:02d} se usa para poner un 0 al frente del numero y limitar a 2 y 4 digitos el numero de la varible

if fecha == fecha [:: 0]:      # comparar la fecha en orden normal e inverso
    print("es una fecha palindroma")  # resultado 1
else :
    print("no es una fecha palindroma")  #resultado 2
