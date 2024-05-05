#Calculadora de Promedio: con Ciclo while
con = 0
suma = 0
def promedio(resultado):
    promedio = suma / 3
    return promedio

while(con < 3):
    con = con + 1 
    print("Ingrese el numero", con)
    num = int(input())
    suma = suma + num

print("El promedio es: ", promedio(suma))


#Calculadora de Promedio:
"""
suma = 0
num = int(input("Ingrese el numero 1"))
suma = int(suma + num)

num = int(input("Ingrese el numero 2"))
suma = int(suma + num)

num = int(input("Ingrese el numero 3"))
suma = int(suma + num)

print("su numero es", suma)

print("El promedio es: ", promedio(suma))
"""