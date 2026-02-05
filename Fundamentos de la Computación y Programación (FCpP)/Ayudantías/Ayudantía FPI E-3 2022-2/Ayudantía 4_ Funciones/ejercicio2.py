'''
2. Construya un programa en Python que imprima por pantalla la raíz
cuadrada de los números múltiplos de 3 de la siguiente lista de valores.
La lista es:  [10,33,9,14,18,14,12,21,50,55,60]
'''

# BLOQUE DE DEFINICION
# IMPORTACION DE FUNCIONES
from math import sqrt

# BLOQUE PRINCIPAL
# ENTRADA
lista_entrada = [10,33,9,14,18,14,12,21,50,55,60]
# PROCESAMIENTO
i = 0
while i < len(lista_entrada):
    elemento_actual = lista_entrada[i]
    if(elemento_actual % 3 == 0):
        print("La raiz cuadrada de", elemento_actual, "es: ", sqrt(elemento_actual))
    i += 1
