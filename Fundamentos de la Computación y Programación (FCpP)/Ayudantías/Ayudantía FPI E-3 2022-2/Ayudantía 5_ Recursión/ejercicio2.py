'''
2. Escriba un programa que calcule el maximo comun divisor de dos numeros enteros
positivos ingresados por el usuario. Utilice para resolver el problema una funcion
recursiva.
'''

# BLOQUE DE DEFINICION
# DEFINICION DE FUNCIONES

def mcd(dividendo, divisor):
    if divisor == 0:
        return dividendo
    else:
        return mcd(divisor, dividendo % divisor)
    
# BLOQUE PRINCIPAL
# ENTRADA
dividendo = int(input("Ingrese el dividendo original: "))
divisor = int(input("Ingrese el divisor original: "))

# PROCESAMIENTO
maximo_comun_divisor = mcd(dividendo, divisor)
# SALIDA
print("El maximo comun divisor es: ", maximo_comun_divisor)
