# UNIDAD 1 -> tipos de datos, operaciones, logicas, condicionales
            # ciclo While, listas y strings
# UNIDAD 2 -> funciones (recursion importaciones)
'''
while [condicion]:
    cuerpo

while 1 > 0: -> mala condicion
    print("hola")

#contador (i)
contador = 0
while contador!= 10:
    print("hola")
    print(contador)
    if contador == 7:
        break
    contador = contador + 2 # contador +=2

# suma: variable = variable + algo == variable +=algo
# resta: variable = variable - algo == variable -=algo

# EL BREAK SE CONSIDERA UNA MALA PRACTICA, NO USAR!
print("se acabo el while")

# los elementos se ingresan juntos para poder obtener
# una lista
a = eval(input("Ingrese algun elemento: "))# ->string
print(a)

#    0 1 2      3           4 5 6
b = [2,3,4,["string",True], 7,3,5]
print(b[3][1])
#     012345678910
c = "hola pepito"
if c[0] == h:
    condicion
else:
    condicion
print(c[0])

Tipos de operaciones con lista:
append : Agrega elementos a una lista
reverse: Da vuelta las posiciones de una lista
sort: Ordena de menor a mayor a una lista
pop: elimina dependiendo de una posicion a un elemento de una lista
remove: Elimina un elemento
+: Me une dos listas
len: Largo de la lista, cuenta la cantidad de elementos
index: Me retorna la posicion de la primera vez que se encuentra
      al elemento
count: Me retorna cuantas veces se tiene un elemento en una lista

lista = [2,3,1,8,9]
i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1 # i += 1

string.upper() : Transforma en ,mayusculas
string.lower(): transforma en minusculas
'''
a = list(input("Ingrese un elemento: "))
print(a)




 
