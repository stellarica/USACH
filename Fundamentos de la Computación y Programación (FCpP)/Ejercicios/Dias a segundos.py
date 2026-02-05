#CONSTANTES
HORAS_POR_DIA = 24
SEGUNDOS_POR_HORA = 3600
#ENTRADA
dias = int(input("Ingrese su cantidad de dias: "))
#PROCESAMIENTO
horas = dias * HORAS_POR_DIA
segundos = horas * SEGUNDOS_POR_HORA
#SALIDA
print(dias,"dias tiene:",segundos,"segundos")
