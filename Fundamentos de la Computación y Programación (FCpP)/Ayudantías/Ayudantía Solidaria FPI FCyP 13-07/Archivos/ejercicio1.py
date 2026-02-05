'''
Dado que Pyuk reprueba alumnos por monton, suele olvidar los alumnos que ha reprobado.
Desarrolle la función reprobado(nombre,archivo) que retorna la causa de reprobacion.
Si no hay causa de reprobacion debe retornar el string "Perdio las ganas de aprobar".
Por ultimo, si el nombre no aparece en la lista, retornar False.
'''

# BLOQUE DE DEFINICIONES
# DEFINICION DE FUNCIONES
'''
Entradas: Un nombre de estudiante y un nombre de un archivo
Salida: Un string que es la causa de reprobacion (o booleano si no esta el nombre)
Descripcion: 
'''
def reprobado(nombre,archivo):
    pynote = open(archivo, "r")
    lineas = pynote.readlines()
    pynote.close()
    flag_encontrado = False
    reprobacion = ""
    for linea in lineas:
        if nombre in linea:
            flag_encontrado = True
            reprobacion = linea
            reprobacion = reprobacion.strip()
    if flag_encontrado:
        if ":" in reprobacion:
            lista_linea = reprobacion.split(":")
            nombre_nota = lista_linea[0]
            lista_nombre_nota = nombre_nota.split("#")
            if nombre == lista_nombre_nota[0]:
                return lista_linea[1]
            else:
                return False
        else:
            if nombre == reprobacion:
                return "Perdio las ganas de aprobar"
            else:
                return False
    else:
        return False
        
# BLOQUE PRINCIPAL

print(reprobado("Naruto Izimiki", "PyNote.txt"))
# PROCESAMIENTO Y SALIDA
