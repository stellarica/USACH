# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 1-C-3
# PROFESOR DE TEORÍA: CRISTIAN SEPÚLVEDA
# PROFESOR DE LABORATORIO: PAULO QUINSACARA
#
# AUTOR
# NOMBRE: John Serrano Carrasco
# RUT:
# CARRERA: Ingeniería Civil Informatica
# DESCRIPCIÓN DEL PROGRAMA: El programa consiste en que el usuario, a traves de la entrada proporciona
# una lista con palabras. El usuario puede ingresar cuantas palabras desee, y el programa calculará
# el puntaje asociado a cada palabra. El programa devolverá por pantalla la palabra que tiene el mayor
# puntaje. Se asume de que el usuario es inteligente y que siempre ingresara una lista de palabras.
# Ademas, se asume de que el usuario solo ingresara palabras que tengan caracteres de la tabla del problema.

# BLOQUE PRINCIPAL
# CONSTANTES
# Escribo la lista de caracteres proporcionada por la tabla del enunciado
LETRA = ['A','B','C','CH','D','E','F','G','H','I','J','K','L','LL','M','N','Ñ','O','P','Q','R','RR','S','T','U','V','W','X','Y','Z','?']
# Escribo la lista de puntajes asociados a los caracteres de la lista anterior
VALOR = [1,3,3,5,2,1,4,2,4,1,8,8,1,8,3,1,8,1,3,5,1,8,1,1,1,4,10,8,4,10,0]
# ENTRADA
# Se ingresa una lista con palabras. Se puede ingresar cuantas palabras se desee.
palabras = eval(input("Ingrese una lista con las palabras deseadas: "))
# PROCESAMIENTO
# Declaro un contador i para poder recorrer listas
i = 0
# Declaro un contador j para poder recorrer listas y strings
j = 0
# Declaro una variable de posicion, para poder guardar la posicion de una letra
posicion = 0
# Declaro una variable de suma, la cual guardara el valor de la suma de los valores de las letras
suma = 0
# Declaro una lista vacia, la cual guardara los puntajes de cada palabra obtenidos de las sumas de los
# valores de las letras
lista_sumas = []
# Mientras no se recorra toda la lista de palabras
while i < len(palabras):
    # Utilizo el metodo .upper() para que la palabra ingresada quede en mayusculas y asi no tener
    # problemas con la lista de letras
    palabra_actual= palabras[i].upper()
    # Mientras no se haya recorrido toda la palabra
    while j < len(palabra_actual):
        # Guardo la letra que se esta revisando en una variable
        letra_actual = palabra_actual[j]
        # Si la letra actual es 'C' y no esta en la ultima posicion de la palabra
        if letra_actual == 'C' and palabra_actual.index(letra_actual) != len(palabra_actual)-1:
            # Si la condicion anterior se cumple y la letra que continua es 'H'
            if palabra_actual[j+1] == 'H':
                # Entonces la letra corresponde a 'CH' y se guardara su posicion en la lista de letra
                # en la variable posicion
                posicion = 3
                # Incremento j para para que asi considere a 'CH' como una sola letra
                j +=1
            # Si la letra siguiente no es 'H'
            else:
                # Se guarda la posicion de la letra 'C' en la variable posicion
                posicion = LETRA.index(palabra_actual[j])
        # Si la letra actual es 'L' y no esta en la ultima posicion de la palabra
        elif letra_actual == 'L'and palabra_actual.index(letra_actual) != len(palabra_actual)-1:
            # Si la condicion anterior se cumple y la letra que continua es 'L'
            if palabra_actual[j+1] == 'L':
                # Entonces la letra corresponde a 'LL' y se guardara su posicion en la lista de letras
                # en la variable posicion
                posicion = 13
                # Incremento j para que asi considere 'LL' como una sola letra
                j += 1
            # Si la letra siguiente no es 'L'
            else:
                # Se guarda la posicion de la letra 'L' en la variable posicion
                posicion = LETRA.index(palabra_actual[j])
        # Si la letra actual es 'R' y no esta en la ultima posicion de la palabra
        elif letra_actual == 'R' and palabra_actual.index(letra_actual) != len(palabra_actual)-1:
            # Si la condicion anterior se cumple y la letra que continua es 'R'
            if palabra_actual[j+1] == 'R':
                # Entonces la letra corresponde a 'RR' y se guardara su posicion en la lista de letras
                # en la variable posicion
                posicion = 21
                # Incremento j para que asi considere 'RR' como una sola letra
                j += 1
            # Si la letra siguiente no es 'R'
            else:
                # Se guarda la posicion de la letra 'R' en la variable posicion
                posicion = LETRA.index(palabra_actual[j])
        # Si no se cumple ninguna de las condiciones anteriores
        else:
            # Guardo la posicion que tiene la letra actual en la lista de letra en la variable posicion
            posicion = LETRA.index(palabra_actual[j])
        # Sumo el puntaje de la letra actual en la variable suma
        suma = suma + VALOR[posicion]
        # Incremento j para que el programa continue recorriendo la palabra
        j+=1
    # Una vez que ya se haya recorrido toda la palabra, guardo el puntaje obtenido a traves de la
    # suma del puntaje de las letras en una lista
    lista_sumas.append(suma)
    # Declaro a j como 0 para que se pueda recorrer la siguiente palabra sin inconvenientes
    j = 0
    # Declaro la suma como 0 para que se puedan guardar los puntajes de la nueva palabra
    suma = 0
    # Incremento i en 1 para que se pueda recorrer la nueva palabra
    i +=1
# Declaro a mayor como 0. Esta variable guardara el puntaje mas alto de la lista de puntajes
mayor = 0
# Declaro i como 0, para poder recorrer la lista de los puntajes
i = 0
# Mientras no se haya recorrido toda la lista de puntajes
while i < len(lista_sumas):
    # Si el puntaje actual es mayor al puntaje guardado en la variable mayor
    if lista_sumas[i] > mayor:
        # Entonces el puntaje actual es el mayor de los puntajes por ahora
        mayor = lista_sumas[i]
    # Incremento i en 1 para poder recorrer toda la lista de puntajes
    i+=1
# Declaro la variable posicion_mayor para poder obtener el index (posicion) del puntaje mayor. Como se
# va agregando a la lista un puntaje por palabra, entonces esta posicion tambien correspondera
# a la posicion de la palabra en la lista ingresada por entrada
posicion_mayor = lista_sumas.index(mayor)
# Guardo en la variable mejor_palabra la palabra a la que le corresponde la mayor puntuacion
mejor_palabra = palabras[posicion_mayor].upper()
# SALIDA
# Finalmente se imprime por pantalla la palabra que octuvo el mayor puntaje y la cantidad de puntaje.
print("La palabra que otorga la mayor cantidad de puntos es:",mejor_palabra,"con",mayor,"puntos")
    
    
