

numero = int(input("Ingrese un numero entero: "))

if numero % 2 ==  0:
    print("El numero", numero, "es par")
else:
    print("El numero", numero, "es impar")

'''
El % te permite saber si un numero es par o impar.
Un numero par al dividirlo por 2 tiene resto 0
Entonces solo debes revisar que el modulo del numero con 2 es 0
Si es asi, el numero es par. Caso contrario, es impar.
Recuerda que el % es el modulo, que corresponde al resto de la
division.
'''
