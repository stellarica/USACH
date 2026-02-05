# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 
# PROFESOR DE TEORÍA: 
# PROFESOR DE LABORATORIO: 
#
# AUTOR
# NOMBRE: 
# RUT: 
# CARRERA: 
# DESCRIPCION: Programa que recibe por entrada una cantidad n de veces que se repite
# una carrera contrarreloj y se van recibiendo tambien mediante entrada, los n tiempos
# de las n veces que se repite la carrera. El programa calcula el peor y mejor tiempo
# junto con las medallas obtenidas e imprime por pantalla el mejor tiempo, el peor
# tiempo, la cantidad de medallas obtenidas y los tiempos ordenados. SE ASUME que
# el usuario siempre va a respetar el formato de entrada de un tiempo, es decir
# que el tiempo sigue el formato x:xx,xxx. Ademas el programa se realizo de tal forma
# de que funcione con numeros enteros negativos y el 0.

# BLOQUE DE DEFINICION
# DEFINICION DE CONSTANTES

# Defino las constantes de los tiempos de medalla en formato String
TIEMPO_ORO = "5:47,914"
TIEMPO_PLATA = "6:01,013"
TIEMPO_BRONCE = "6:03,607"

# BLOQUE PRINCIPAL
# ENTRADA
# Solicito un numero de veces que se repite la carrera
numero_carrera = abs(int(input("Ingrese el numero de veces que se realiza la carrera: ")))
# Defino un iterador solicitar n tiempos
i = 0
# Defino una lista vacia donde se van a ir guardando los n tiempos
lista_tiempos = []
# Mientras i sea menor a la cantidad de veces que se repite la carrera
while i < numero_carrera:
    # Solicito un tiempo de carrera
    tiempo_carrera = input("Ingrese el tiempo " + str(i+1) + ": ")
    # Agrego el tiempo de carrera a la lista de tiempos
    lista_tiempos.append(tiempo_carrera)
    # Aumento el iterador para que se pueda seguir recorriendo el ciclo while
    i += 1

# PROCESAMIENTO
# Defino las variables para las medallas de oro, plata y bronce
medallas_oro = 0
medallas_plata = 0
medallas_bronce = 0
# Defino las variables para el mejor y peor tiempo
mejor_tiempo = ""
peor_tiempo = ""
# Ordeno la lista de los tiempos
lista_tiempos.sort()
# Defino un iterador para recorrer la lista de tiempos
j = 0
# Mientras j sea menor a la cantidad de tiempos de carrera
while j < len(lista_tiempos):
    # Obtengo un tiempo de carrera
    tiempo_actual = lista_tiempos[j]
    # Si el tiempo actual es menor al tiempo de la medalla de oro
    if(tiempo_actual < TIEMPO_ORO):
        # Obtengo una medalla de oro
        medallas_oro += 1 # medallas_oro = medallas_oro + 1
    # Si el tiempo actual es menor al tiempo de la medalla de plata
    elif(tiempo_actual < TIEMPO_PLATA):
        # Obtengo una medalla de plata
        medallas_plata += 1
    # Si el tiempo actual es menor al tiempo de la medalla de bronce
    elif(tiempo_actual < TIEMPO_BRONCE):
        # Obtengo de medalla de bronce
        medallas_bronce += 1
    # Si el tiempo actual es mayor al tiempo de la medalla de bronce entonces
    # no obtengo ninguna medalla

    # Aumento el contador en 1 para seguir iterando
    j += 1

# Si realizo la carrera al menos 1 vez
if(len(lista_tiempos) != 0):
    # Obtengo el mejor tiempo el cual es el primer tiempo de la lista ordenada
    mejor_tiempo = lista_tiempos[0]
    # Obtengo el peor tiempo el cual es el ultimo tiempo de la lista ordenada
    peor_tiempo = lista_tiempos[len(lista_tiempos) - 1]

# SALIDA
print("---------------------------------------")
print("El mejor tiempo es:", mejor_tiempo)
print("El peor tiempo es:", peor_tiempo)
print("La cantidad de medallas de oro es:", medallas_oro)
print("La cantidad de medallas de plata es:", medallas_plata)
print("La cantidad de medallas de bronce es:", medallas_bronce)
print("")
print("Los tiempos de la carrera en orden de menor a mayor son:")
# Declaramos un iterador para recorrer de tiempos
k = 0
# Mientras k sea menor a la cantidad de tiempos
while k < len(lista_tiempos):
    # Imprimimos los tiempos en orden de menor a mayor.
    print("Tiempo " + str(k+1) + ":", lista_tiempos[k])
    k += 1
