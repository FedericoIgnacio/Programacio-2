#Conversor de Temperatura
print ("Eliga que temperatura quiere convertir:")
print ("Celcius --> Fahrenheit (1)")
print ("Celcius <-- Fahrenheit (2)")
valor = int(input())

celcius = 0
Fahrenheit = 0

if(valor == 1):
    celcius = int(input("Ingrese la temperatura en celcius "))
    Fahrenheit = (celcius * 9/5) + 32
    print (Fahrenheit)

if(valor == 2):
    Fahrenheit = int(input("Ingrese la temperatura en fahrenheit "))
    celcius = 5/9 *(Fahrenheit - 32)
    print (celcius)