# BLOQUE DE DEFINICIONES
# DEFINICION DE CONSTANTES

# BLOQUE PRINCIPAL
# ENTRADA
lista = eval(input("Ingrese una lista: "))
# PROCESAMIENTO
estan_todos = True # FLAG # Bandera
n = len(lista)
numero = 1 # Esto inicia desde 1 y debe llegar hasta n
while numero <= n:
    numero_actual = False # Asumo que el numero actual no esta en la lista
    posicion_lista = 0 # Iterador
    while posicion_lista < n:
        if numero == lista[posicion_lista]:
            numero_actual = True  # Si se encontro el numero en la lista
        posicion_lista += 1
    if numero_actual == False:
        estan_todos = False
        numero = n+1
    numero += 1
# SALIDA
if(estan_todos):
    print("Si estan todos los numeros desde el numero 1 hasta el numero", n)
else:
    print("No se encontraron todos los numeros")

    
