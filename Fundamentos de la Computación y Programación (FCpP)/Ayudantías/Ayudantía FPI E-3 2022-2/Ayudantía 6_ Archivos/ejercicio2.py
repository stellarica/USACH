'''
Desarrolle la función agregar(lista, archivo), que reciba una lista con el nombre,
nota (int) y la causa de reprobación o solo el nombre de un nuevo alumno.
La función debe agregar una línea con la información de la lista al
final de la PyNote.
'''

# BLOQUE DE DEFINICION
# DEFINICION DE FUNCIONES
def agregar(lista, archivo):
    pynote = open(archivo, "a")
    if len(lista) == 3:
        texto = "\n" + lista[0] + "#" + str(lista[1]) + ":" + lista[2] + "."
        pynote.write(texto)
        pynote.close()
        return "Se modifico el archivo con exito"
    elif len(lista) == 1:
        texto = "\n" + lista[0]
        pynote.write(texto)
        pynote.close()
        return "Se modifico el archivo con exito"
    else:
        return "No se pudo modificar el archivo"

# PROCESAMIENTO Y SALIDA

print(agregar([], "PyNote.txt"))
