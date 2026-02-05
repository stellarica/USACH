temperatura_maxima = eval(input("Ingrese una lista de Temperaturas Maximas: "))
numero = int(input("Ingrese un numero: "))
n = len(temperatura_maxima)
i = 0
lista = []
while i < len(temperatura_maxima) - 1:
    indice_minimo = i
    j = i + 1
    while j < len(temperatura_maxima):
        if temperatura_maxima[j] < temperatura_maxima[indice_minimo]:
            indice_minimo = j
        j = j + 1
    aux = temperatura_maxima[i]
    temperatura_maxima[i] = temperatura_maxima[indice_minimo]
    temperatura_maxima[indice_minimo] = aux
    i = i + 1
while numero -1 < n:
      lista.append(temperatura_maxima[n-1])
      n-=1
if numero < len(temperatura_maxima):
     print("Las",numero,"temperaturas mas altas son:",lista)
else:
     print("Debe ingresar un numero menor al largo de  la lista ingresada")

