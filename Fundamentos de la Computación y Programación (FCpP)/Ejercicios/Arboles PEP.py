#Primavera - Verano - Otono - Invierno
'''Descripción del programa: Programa que calcula cuanto tiempo
le toma a un arbol alcanzar una altura determinada de acuerdo al enunciado del problema'''
#BLOQUE PRINCIPAL
#CONSTANTES
DURACION_ESTACION = 3
PRIMAVERA = 0.3
VERANO = 1
OTONO = 0.05
#ENTRADA
valorAltura = abs(float(input("Ingrese una altura en metros: ")))
#PROCESAMIENTO
altura = 0.5
meses = 0
pri = True
ver = False
oto = False
inv = False
while altura <= valorAltura:
    if pri:
        if altura <= valorAltura:
            altura = altura + altura*PRIMAVERA
            meses+=3
            pri = False
            ver = True
    if ver:
        if altura <= valorAltura: 
            altura = altura + 1
            meses +=3
            ver = False
            oto = True
    if oto:
        if altura <= valorAltura:
            altura = altura + altura*OTONO
            meses +=3
            oto = False
            inv = True
    if inv:
        if altura<= valorAltura:
            meses +=3
            inv = False
            pri = True
#SALIDA
print("El tiempo que le toma al arbol en alcanzar",valorAltura,"metros es:",meses,"meses")
