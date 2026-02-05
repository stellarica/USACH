'''DESCRIPCIÓN DEL PROGRAMA: Programa que calcula cual es la mayor suma entre las sublistas
de una lista. Se considera de que el usuario es inteligente y siempre ingresara una lista de
sublistas.'''
#BLOQUE PRINCIPAL
#ENTRADA
lista = eval(input("Ingrese una lista de sublistas: "))
#PROCESAMIENTO
i = 0
suma = 0
while i < len(lista):
    if sum(lista[i]) > suma:
        suma = sum(lista[i])
    i+= 1
i = 0
while i < len(lista):
    if suma == sum(lista[i]):
        mayor = lista[i]
    i+=1
#SALIDA
print("La sublista con mayor suma es:",mayor)
