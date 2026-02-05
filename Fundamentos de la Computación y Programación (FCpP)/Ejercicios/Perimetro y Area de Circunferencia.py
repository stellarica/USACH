'''
Construya un programa que calcule el area y perimetro
de una circunferencia
'''

#CONSTANTES
PI = 3.1415926535

#ENTRADA
radio = int(input("Ingrese el radio de la circunferencia: "))

#PROCESO
perimetro = 2 * radio * PI
area = PI * (radio **2)

#SALIDA
print("El perimetro de la circunferencia de radio",radio,"es : ",perimetro)
print("El area de la circunferencia de radio",radio,"es : ",area)
