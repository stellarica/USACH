numero_1 = abs(int(input("Ingrese un numero entero: ")))
numero_2 = abs(int(input("Ingrese un numero entero: ")))

i = 0
j = 0
contador = 0
string = str(numero_1) + "*" + str(numero_2)
while i < numero_2:
    contador = contador + numero_1
    if i == 0:
        string = string + "=" + str(numero_1) + "+"
    elif i == (numero_2 - 1):
        string = string + str(numero_1)
    else:
        string = string + str(numero_1) + "+"
    i += 1
    
string = string + "=" + str(contador)
print("El resultado de", str(numero_1),"*", str(numero_2), "es", contador)
print(string)
