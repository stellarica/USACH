'''Construya un programa en Python que reciba como entrada un string y
determine cual es la letra que mas se repite.
Restriccion: no utilice el m ́etodo count()'''

'''NOTA: A pesar de que este ejercicio proviene de una guia de funciones,
el ejercicio se puede realizar sin la necesidad de definir alguna funcion'''

# BLOQUE PRINCIPAL
# ENTRADA
palabra = input("Ingrese una palabra: ").lower()
# PROCESAMIENTO
i = 0
palabra = list(palabra)
valores = []
letras = []
while i < len(palabra):
    num = 0
    j = 0
    letra = palabra[i]
    if letra not in letras:
        while j < len(palabra):
            if palabra[j] == letra:
                num += 1
            j += 1
        valores.append(num)
        letras.append(letra)
    i += 1

maximo = max(valores)
indice = valores.index(maximo)
letra_repetida = letras[indice]

# SALIDA
print("La letra que mas se repite es la letra", letra_repetida)

    
