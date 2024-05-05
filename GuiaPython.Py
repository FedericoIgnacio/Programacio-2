#Calculadora de Promedio
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