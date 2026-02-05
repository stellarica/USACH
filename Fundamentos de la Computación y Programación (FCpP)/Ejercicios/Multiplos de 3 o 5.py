'''DESCRIPCION DEL PROGRAMA: Programa que calcula los multiplos de 3 o 5
entre un intervalo de numeros (extremos incluidos)'''
#BLOQUE PRINCIPAL
#ENTRADA
inicio = int(input("Ingrese un numero de inicio: "))
fin = int(input("Ingrese un numero de fin: "))
#PROCESAMIENTO
multiplo = 0
if inicio <= fin:
    while inicio <= fin:
        if inicio%3 == 0 or inicio %5 == 0:
            multiplo +=1
        inicio+=1
#SALIDA
print("Existen",multiplo,"numeros multiplos de 3 o de 5")

    
