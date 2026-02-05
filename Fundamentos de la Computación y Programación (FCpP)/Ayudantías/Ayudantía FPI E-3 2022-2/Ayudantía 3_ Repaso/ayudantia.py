# BLOQUE DE DEFINICION
# DEFINICION DE CONSTANTES

# BLOQUE PRINCIPAL
# ENTRADA
precios_de_pelotas = eval(input("Ingrese la lista de precios de pelotas: "))
precios_de_camisetas = eval(input("Ingrese la lista de precios de camisetas: "))
presupuesto = int(input("Ingrese el presupuesto: "))

# PROCESAMIENTO
monto_gasto = 0
i = 0
while i < len(precios_de_pelotas):
    j = 0
    while j < len(precios_de_camisetas):
        monto = precios_de_pelotas[i] + precios_de_camisetas[j]
        if(monto <= presupuesto) and (monto > monto_gasto):
            monto_gasto = monto
        j += 1
    i += 1
# SALIDA
if(monto_gasto == 0):
    print("No habia ningun par de pelotas y camisetas que se acercara al presupuesto")
else:
    print("El monto que se acerca al presupuesto es: ", monto_gasto)

    
