'''Descripcion del programa: El usuario entrega dos listas y se verifica de que
la lista B tenga todos los elementos de A elevados al cuadrado. La repetición si
cuenta. Se asume de que el usuario siempre ingresara dos listas.'''
#BLOQUE PRINCIPAL
#ENTRADA
listaA = eval(input("Ingrese la lista A: "))
listaB = eval(input("Ingrese la lista B: "))
#PROCESAMIENTO
pseudovalentes = True
i = 0
if len(listaA) != len(listaB):
    pseudovalentes = False

while i < len(listaA) and pseudovalentes:
    if listaA[i]**2 not in listaB:
        pseudovalentes = False
    i+= 1

i = 0
while i < len(listaB) and pseudovalentes:
    if listaB[i]**0.5 not in listaA:
        pseudovalentes = False
    i+= 1
    
if pseudovalentes:
    i = 1
    while i < len(listaA):
        clave = listaA[i]
        j = i - 1
        while j >= 0 and clave < listaA[j]:
            listaA[j + 1] = listaA[j]
            j = j - 1
        listaA[j + 1] = clave
        i+=1
    i = 1
    while i < len(listaB):
        clave = listaB[i]
        j = i - 1
        while j >= 0 and clave < listaB[j]:
            listaB[j + 1] = listaB[j]
            j = j - 1
        listaB[j + 1] = clave
        i+=1
    i = 0
    while i < len(listaA):
        if listaA[i] **2 != listaB[i]:
            pseudovalentes = False
        i+=1
#SALIDA
if pseudovalentes == False:
    print(False)
else:
    print(True)
