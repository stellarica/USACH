# IMPORTACION DE FUNCIONES
from math import pi

# DEFINICION DE FUNCIONES

def obtener_maximo(lista):
    '''
    Entrada: Una lista de numeros enteros
    Salida: Un numero entero correspondiente al maximo de una lista
    Descripcion: Funcion que recorre una lista de numeros enteros y obtiene
    su maximo sin utilizar la funcion nativa max().
    '''
    i = 0
    maximo = lista[0]
    while i < len(lista):
        if lista[i] > maximo:
            maximo = lista[i]
        i += 1
    return maximo


def operar_cada_elemento(lista_num):
    '''
    Entrada: Una lista de numeros enteros
    Salida: Una lista de numeros flotantes
    Descripcion: Funcion que recorre una lista de numeros enteros y
    multiplica cada elemento con el valor de PI. Devuelve la lista modificada.
    '''
    i = 0
    lista = []
    while i < len(lista_num):
        lista.append(lista_num[i] * pi)
        i += 1
    return lista
