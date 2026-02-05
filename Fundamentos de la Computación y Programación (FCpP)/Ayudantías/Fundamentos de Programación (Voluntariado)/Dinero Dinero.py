'''
Construya un programa que reciba una cantidad de dinero e informe al usuario el
desglose de dicha cantidad en la menor cantidad de billetes y monedas posibles
'''

#ENTRADA
dinero = int(input("Ingrese la cantidad de dinero: "))

#PROCESO
billetes_de_20 = dinero //20000
resto1 = dinero%20000
billetes_de_10 = resto1 //10000
resto2= resto1%10000
billetes_de_5 = resto2 // 5000
resto3 = resto2%5000
billetes_de_2 = resto3 // 2000
resto4 = resto3 % 2000
billetes_de_1 = resto4 // 1000
resto5 = resto4 % 1000
monedas_de_500 = resto5 //500
resto6 = resto5 % 500
monedas_de_100 = resto6 // 100
resto7 = resto6 % 100
monedas_de_50 = resto7 // 50
resto8 = resto7 % 50
monedas_de_10 = resto8 // 10
resto9 = resto8 % 10
monedas_de_5 = resto9 // 5
resto10 = resto9 % 5
monedas_de_1 = resto10 // 1

#SALIDA
print("La cantidad de billetes de 20 es:",billetes_de_20)
print("La cantidad de billetes de 10 es:",billetes_de_10)
print("La cantidad de billetes de 5 es:",billetes_de_5)
print("La cantidad de billetes de 2 es:",billetes_de_2)
print("La cantidad de billetes de 1 es:",billetes_de_1)
print("La cantidad de monedas de 500 es:",monedas_de_500)
print("La cantidad de monedas de 100 es:",monedas_de_100)
print("La cantidad de monedas de 50 es:",monedas_de_50)
print("La cantidad de monedas de 10 es:",monedas_de_10)
print("La cantidad de monedas de 5 es:",monedas_de_5)
print("La cantidad de monedas de 1 es:",monedas_de_1)
