# EXPLICACION DEL CODIGO: Codigo que recibe valores separados por espacios
# como entrada devuelve el promedio y la desviacion estandar de esos valores.
# BLOQUE DE DEFINICIONES
# DEFINICION DE FUNCIONES


def promedio(lista_valores):
    # Funcion que calcula el promedio de los valores
    # Entrada: La lista de los valores
    # Salida: Promedio de los valores
    suma = 0
    i = 0
    while i < len(lista_valores):
        suma = float(lista_valores[i]) + suma
        i += 1
    suma = suma / len(lista_valores)
    return suma


def desviacion(lista_valores):
    # Funcion que calcula la desviacion estandar de los valores
    # Entrada: La lista de los valores
    # Salida: Descviacion estandar de los valores
    suma = 0
    i = 0
    while i < len(lista_valores):
        suma = ((float(lista_valores[i]) - prom) ** 2) + suma
        i += 1
    suma = suma / len(lista_valores)
    suma = suma ** 0.5
    return suma


# BLOQUE PRINCIPAL
# ENTRADA
valores = input("Ingrese valores separados por espacio: ")
# PROCESAMIENTO
lista_valores = valores.split()
prom = promedio(lista_valores)
desv = desviacion(lista_valores)
# SALIDA
print("El promedio es:", prom)
print("La desviacion estandar es:", desv)
