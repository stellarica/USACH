# BlOQUE DE DEFINICION
# IMPORTACION DE FUNCIONS
from definicion_funciones import obtener_maximo
from definicion_funciones import operar_cada_elemento

# BLOQUE PRINCIPAL
# ENTRADA
# BLOQUE PRINCIPAL
# ENTRADA
lista_numeros = eval(input("Ingrese una lista de numeros enteros: "))

# PROCESAMIENTO
maximo = obtener_maximo(lista_numeros)  # Se llama a la funcion obtener_maximo
lista_numeros2 = operar_cada_elemento(lista_numeros)  # Se llama a la funcion operar_cada_elemento
maximo2 = obtener_maximo(lista_numeros2)   # Se llama a la funcion obtener_maximo

# SALIDA
print("La lista original es: ", lista_numeros)
print("El maximo de esta lista es: ", maximo)
print("\n")
print("La lista al llamar a la funcion operar_cada_elemento es: ", lista_numeros2)
print("El maximo de esta lista es: ", maximo2)
