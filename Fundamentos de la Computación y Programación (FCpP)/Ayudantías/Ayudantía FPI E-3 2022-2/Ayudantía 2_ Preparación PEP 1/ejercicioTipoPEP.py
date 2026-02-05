# DATOS 

# BLOQUE DE DEFINICIONES
# DEFINICION DE CONSTANTES
VOCALES = ["a","e","i","o","u"]

# BLOQUE PRINCIPAL
# ENTRADA
palabra = input("Ingrese una palabra: ").lower()
# PROCESAMIENTO

secuencia_mayor_largo = 0
i = 0
while i < len(palabra):
    if palabra[i] in VOCALES: # Si la letra esta dentro de la lista VOCALES
        secuencia = 1
        vocal = True # Una cadena de vocales
        j = i + 1
        while j < len(palabra) and vocal:
            if palabra[j] in VOCALES:
                secuencia += 1
            else:
                vocal = False
            j += 1
        i = j
        if secuencia > secuencia_mayor_largo:
            secuencia_mayor_largo = secuencia
    else:
        i += 1 
# SALIDA

print("La secuencia mas larga de vocales es de largo:", secuencia_mayor_largo) 


'''
Queda pendiente mostrar cual es la secuencia!
'''
