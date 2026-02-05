A = eval(input("Ingrese una lista de numeros: "))
B = eval(input("Ingrese otra lista de numeros: "))

i = 0
numeros = []
interseccion = []
while i < len(A):
    if A[i] not in numeros:
        numeros.append(A[i])
    i+=1
i = 0
while i < len(numeros):
    if numeros[i] in A and numeros[i] in B:
        interseccion.append(numeros[i])
    i +=1
interseccion.sort()
print("La interseccion es:",interseccion)
    
