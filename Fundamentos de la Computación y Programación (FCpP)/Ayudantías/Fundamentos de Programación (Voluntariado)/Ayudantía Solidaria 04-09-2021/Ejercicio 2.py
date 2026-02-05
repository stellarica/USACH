# BLOQUE PRINCIPAL
# ENTRADAS
lado_a = float(input("Ingrese el lado a: "))
lado_b = float(input("Ingrese el lado b: "))
lado_c = float(input("Ingrese el lado c: "))
# PROCESAMIENTO
s = (lado_a +lado_b + lado_c) / 2
area = ((s*(s-lado_a)*(s-lado_b)*(s-lado_c)))**0.5
# SALIDA
print(area)
