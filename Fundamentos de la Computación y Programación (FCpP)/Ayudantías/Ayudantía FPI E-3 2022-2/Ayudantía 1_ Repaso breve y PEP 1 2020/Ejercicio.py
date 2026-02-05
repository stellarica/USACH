# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 
# PROFESOR DE TEORÍA: 
# PROFESOR DE LABORATORIO:
#
# AUTOR
# NOMBRE: 
# RUT: 
# CARRERA:
# DESCRIPCIÓN DEL PROGRAMA:


# BLOQUE DE DEFINICION
# DEFINICION DE CONSTANTES
LETRAS = ["A","B","C","CH","D","E","F","G","H",
          "I","J","K","L","LL","M","N","Ñ","O",
          "P","Q","R","RR","S","T","U","V","W",
          "X","Y","Z","?"]

VALOR = [1,3,3,5,2,1,4,2,4,1,8,8,1,8,3,1,8,1,3,
         5,1,8,1,1,1,4,10,8,4,10,0]

# BLOQUE PRINCIPAL
# ENTRADA
# Se imgresa una lista con palabras
lista_palabras = eval(input("Ingrese una lista de palabras: "))
# PROCESAMIENTO
# Declaro iteradores
i = 0
j = 0
# Declaro una variable posicion en la lista LETRAS y VALOR
posicion = 0
# Declaro la variable suma para guardar la suma de las letras
suma = 0
# Declaro una lista donde voy a ir guardando los puntajes de las palabras PROGRAC
lista_sumas = []
# Recorro la lista de entrada
while i < len(lista_palabras):
    # Obtengo una palabra de la lista
    palabra_actual = lista_palabras[i].upper()
    # Recorro la palabra actual
    while j < len(palabra_actual):
        # Obtengo una letra actual
        letra_actual = palabra_actual[j]
        if (letra_actual == "C") and (palabra_actual.index(letra_actual) != (len(palabra_actual) - 1)):
            if(palabra_actual[j+1] == "H"):
                posicion = 3 # ACA GUARDO LA POSICION DE CH
                j += 1
            else:
                posicion = LETRAS.index(palabra_actual[j]) # guardo la posicion de C
        elif (letra_actual == "L") and (palabra_actual.index(letra_actual) != (len(palabra_actual) - 1)):
            if(palabra_actual[j+1] == "L"):
                posicion = 13
                j += 1
            else:
                posicion = LETRAS.index(palabra_actual[j])
        elif (letra_actual == "R") and (palabra_actual.index(letra_actual) != (len(palabra_actual) - 1)):
            if(palabra_actual[j+1] == "R"):
                posicion = 21
                j +=1
            else:
                posicion = LETRAS.index(palabra_actual[j])
        else:
            posicion = LETRAS.index(palabra_actual[j])
        suma = suma + VALOR[posicion]
        j+= 1
    lista_sumas.append(suma)
    j = 0
    suma = 0
    i += 1

# SALIDA
print(lista_sumas)

'''
TAREA: Analice el código, comente lo que falte y termine el ejercicio
¿Como podemos obtener el maximo de una lista sin usar max()?
Tip: Utilice un ciclo WHILE
'''
