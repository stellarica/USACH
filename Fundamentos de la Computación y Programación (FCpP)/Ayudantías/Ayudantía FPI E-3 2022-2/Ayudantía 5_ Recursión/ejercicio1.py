'''
1. Escriba en Python un programa que ordene de menor a mayor una lista de enteros
ingresada por teclado utilizando la siguiente idea: ubique el menor numero de
la lista en la primera posicion, y luego ordene el resto de la lista con una
llamada recursiva.
'''

# BLOQUE DE DEFINICION
# DEFINCION DE FUNCIONES
def ordenar_lista(lista):
    if len(lista) <= 1:
        return lista
    else:
        posicion_menor_elemento = lista.index(min(lista))
        variable_temporal = lista[0]
        lista[0] = lista[posicion_menor_elemento]
        lista[posicion_menor_elemento] = variable_temporal
        return [lista[0]] + ordenar_lista(lista[1:])
    
# BLOQUE PRINCIPAL
# ENTRADA
lista = eval(input("Ingrese una lista de numeros enteros: "))

# PROCESAMIENTO
lista_ordenada = ordenar_lista(lista)

# SALIDA
print("La lista ordenada es: ", lista_ordenada)
