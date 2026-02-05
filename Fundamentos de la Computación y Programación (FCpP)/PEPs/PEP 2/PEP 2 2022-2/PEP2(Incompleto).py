# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: E-3
# PROFESOR DE TEORÍA: CRISTIAN SEPULVEDA
# PROFESOR DE LABORATORIO: 
#
# AUTOR
# NOMBRE: 
# RUT: 
# CARRERA: Ingeniería Civil
# DESCRIPCION: 

# BLOQUE DE DEFINICIONES

# IMPORTACION DE FUNCIONES
import numpy as np
import pandas as pd

# DEFINICION DE FUNCIONES

def leer_archivo(nombre_archivo):
    dataframe = pd.read_csv(nombre_archivo, sep = ";")
    return dataframe

def obtener_paises(participantes):
    paises = participantes["pais"]
    return paises

def obtener_identificador(participantes):
    identificador_unico = participantes["identificador"]
    return identificador_unico

def obtener_tiempo(identificador, tiempos):
    tiempos_participante = tiempos[tiempos["identificador"] == identificador]
    return tiempos_participante

def obtener_apodo(identificador, participantes):
    apodo = participantes[participantes["identificador"] == identificador]
    apodo = apodo["apodo"]
    return apodo

def calculo_tiempo(tiempo1, tiempo2):
    carry = 0
    tiempo1 = tiempo1.split(":")
    tiempo2 = tiempo2.split(":")
    tiempo1_mili = tiempo1[2].split(",")
    tiempo2_mili = tiempo2[2].split(",")
    milisegundos = int(tiempo1_mili[1]) + int(tiempo2_mili[1])
    if milisegundos >= 1000:
        milisegundos = milisegundos - 1000
        carry = carry + 1
    segundos = int(tiempo1_mili[0]) + int(tiempo2_mili[0])
    if carry > 0:
        segundos = segundos + carry
        carry = carry - 1
    if segundos >= 100:
        segundos = segundos - 100
        carry = carry + 1
    minutos = int(tiempo1[1]) + int(tiempo2[1])
    if carry > 0:
        minutos = minutos + carry
        carry = carry - 1
    if minutos >= 100:
        minutos = minutos - 100
        carry = carry + 1
    horas = int(tiempo1[0]) + int(tiempo2[0])
    if carry > 0:
        horas = horas + carry
        carry = carry - 1

    if milisegundos < 10:
        milisegundos = "00" + str(milisegundos)
    elif milisegundos < 100:
        milisegundos = "0" + str(milisegundos)
    else:
        milisegundos = str(milisegundos)
        

    if segundos < 10:
        segundos = "0" + str(segundos)
    else:
        segundos = str(segundos)
        
    if minutos < 10:
        minutos = "0" + str(minutos)
    else:
        minutos = str(segundos)
        
    tiempo_final_str = str(horas) + ":" + minutos + ":" + segundos + "," + milisegundos
    return tiempo_final_str
    

def calcular_tiempo(tiempos_participantes):
    indices_tiempos = tiempos_participantes.index
    k = 0
    tiempos_participantes = tiempos_participantes["tiempo"]
    times = []
    while k < len(indices_tiempos):
        times.append(tiempos_participantes[indices_tiempos[k]])
        k += 1
    k = 0
    resultado = calculo_tiempo(times[0], times[1])
    resultado = calculo_tiempo(resultado, times[2])
    resultado = calculo_tiempo(resultado, times[3])
    resultado = calculo_tiempo(resultado, times[4])
    return resultado
# DEFINICION DE CONSTANTES

# BLOQUE PRINCIPAL
# ENTRADA
participantes = leer_archivo("Participantes.csv")
tiempos = leer_archivo("Tiempos.csv")

# PROCESAMIENTO
codigos_paises = obtener_paises(participantes)

i = 0
while i < len(codigos_paises):
    resultados = []
    nombres = []
    correo = []
    corredores_pais = participantes[participantes["pais"] == codigos_paises[i]]
    identificadores_unicos = obtener_identificador(corredores_pais)
    indices = identificadores_unicos.index
    j = 0
    while j < len(indices):
        tiempos_participante = obtener_tiempo(identificadores_unicos[indices[j]], tiempos)
        if len(tiempos_participante) == 5:
            tiempo_total = calcular_tiempo(tiempos_participante)
            resultados.append(tiempo_total)
        apodo_participante = obtener_apodo(identificadores_unicos[indices[j]], participantes)
        nombres.append(apodo_participante)
        j += 1
    resultados.sort()
    i += 1
# SALIDA
