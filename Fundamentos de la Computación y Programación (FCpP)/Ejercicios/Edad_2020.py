'''
Construya un programa donde al usuario se le pregunte su año y se le entregue
su edad de acuerdo al año actual
'''

#CONSTANTES
AÑO = 2020

#ENTRADA
nacimiento_año = int(input("Ingrese el año de nacimiento: "))

#PROCESO
edad = AÑO - nacimiento_año

#SALIDA
print("Tu edad es: ",edad)
