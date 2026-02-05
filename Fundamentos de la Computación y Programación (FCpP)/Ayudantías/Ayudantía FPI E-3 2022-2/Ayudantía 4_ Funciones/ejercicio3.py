'''
Construya un programa en Python que reciba como entrada un string y determine cuál
es la letra que más se repite.
Restricción: no utilice el método count()
'''

# BLOQUE DE DEFINICION
# DEFINICION DE FUNCIONES
def obtener_valor(string, caracter):
    j = 0
    valor = 0
    while j < len(string):
        if caracter == string[j]:
            valor += 1
        j += 1
    return valor

def obtener_mas_repetido(lista_unicos, lista_valores):
    maximo_valor = max(lista_valores)
    posicion = lista_valores.index(maximo_valor)
    return lista_unicos[posicion]

# BLOQUE PRINCIPAL
# ENTRADA
string = input("Ingrese un string: ")
# PROCESAMIENTO
lista_unicos = []
lista_valores = []
i = 0
while i < len(string):
    caracter_actual = string[i]
    if caracter_actual not in lista_unicos:
        valor_actual = obtener_valor(string, caracter_actual)
        lista_unicos.append(caracter_actual)
        lista_valores.append(valor_actual)
    i += 1

caracter_mas_repetido = obtener_mas_repetido(lista_unicos, lista_valores)

# SALIDA
print("El caracter mas repetido es:", caracter_mas_repetido)
