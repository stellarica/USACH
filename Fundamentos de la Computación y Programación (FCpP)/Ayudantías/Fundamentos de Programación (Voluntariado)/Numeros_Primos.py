# Entrada
numero = int(input("Ingrese un numero: "))

# Procesamiento

# Si el numero es mayor que 1, es candidato a primo
if numero > 1:
    flag = True
# Si el numero es menor que 1, no es primo
else:
    flag = False
# Se crea un contador equivalente al numero - 1
contador = numero - 1
# Mientras el contador sea mayor que 1
while contador > 1:
    # Vamos a verificar si tiene divisores que no sean el
    # mismo numero y el 1
    if numero % contador == 0:
        # Si es asi, entonces el numero no es primo
        flag = False
    # Se disminuye el contador para seguir verificando los
    # demas numeros
    contador = contador - 1
# Si flag es True (es primo)
if flag:
    print("El numero", numero, "es primo")
# Si flag es False (no es primo)
else:
    print("El numero", numero, "no es primo")
