# -*- coding: cp1252 -*-
# Calcula los primeros n términos de una serie

# DATOS DE ENTRADA
# Solicita un número
numero = int(input("Ingrese el número de términos de la serie: "))
# Inicializa la variable iteradora
k = 1
# Inicializa la variable acumuladora
suma = 0

# PROCESAMIENTO
while k <= numero:
    # Calcula los resultados parciales
    suma = suma + ((k ** 2 + 2)/(k ** 3 + 6 * k))
    # Incremeta el iterador
    k = k + 1

# SALIDA
print("La suma de los primeros", numero, "términos de la serie es: ", suma)
