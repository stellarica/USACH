'''
Las reglas de la PyNote dicen que si un nombre es tachado antes de reprobar,
este aprobará todos sus ramos. Escriba la función tachar(nombre, archivo)
que modifique el nombre de la persona en el archivo, tachando todas sus letras
con un guion (-). Considere que el nombre siempre estara en el archivo.
'''

# BLOQUE DE DEFINICIONES
# DEFINICION DE FUNCIONES

def tachar(nombre, archivo):
    pynote = open(archivo, "r")
    lineas = pynote.readlines()
    pynote.close()
    for linea in lineas:
        if nombre in linea:
            posicion = lineas.index(linea)
            reprobacion = linea
            reprobacion = reprobacion.strip()
    if "#" in reprobacion:
        linea_nombre = reprobacion.split("#")
        nuevo_texto = "-" * len(linea_nombre[0])
        nuevo_texto = nuevo_texto + "#" + linea_nombre[1]
        if posicion != len(lineas) - 1:
            nuevo_texto = nuevo_texto + "\n"
        lineas[posicion] = nuevo_texto
    else:
        nuevo_texto = "-" * len(reprobacion)
        if posicion != len(lineas) - 1:
            nuevo_texto = nuevo_texto + "\n"
        lineas[posicion] = nuevo_texto
    i = 0
    texto = ""
    while i < len(lineas):
        texto = texto + lineas[i]
        i += 1
    pynote = open(archivo, "w")
    pynote.write(texto)
    pynote.close()
    return "Se ha modificado el archivo con exito"

# BLOQUE PRINCIPAL

# PROCESAMIENTO Y SALIDA
print(tachar("Fabiola Misa", "PyNote.txt"))

