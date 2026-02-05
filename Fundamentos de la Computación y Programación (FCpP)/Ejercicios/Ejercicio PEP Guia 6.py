'''Ejercicio 19  Guía 6 C-3'''
'''Descripcion del programa:
Entrega listas de alumnos aprobados, reprobados, alumnos que deban dar examen,
mejor nota, peor nota y promedio total, de acuerdo a la entrada del listado
de calificaciones.'''
#ENTRADA
#Solicito el listado de calificaciones, con el nombre y nota de cada estudiante
calificaciones = eval(input("Ingrese una lista de listas: "))

#PROCESAMIENTO
#Se asignan contadores que se utilizaran para recorrer las listas
i = 0
mi = 0
ma = 0
me = 0
final = 0
flag = True
#Se asignan listas vacias, cuyos nombres representan lo que se almacenara
aprobados = []
reprobados = []
examen = []
notas = []
mejor = []
peor = []
#Recorremos por primera vez el listado de calificaciones
while i < len(calificaciones):
      #Si la calificacion es mayor a 4.0, se agrega el nombre a la lista de aprobados
      if calificaciones[i][1] >= 4.0:
            aprobados.append(calificaciones[i][0])
      #Si la calificacion esta entre 3.0 y 3.9, se agrega el nombre a la lista de examen
      elif calificaciones[i][1] >= 3.0 and calificaciones[i][1] <= 3.9:
            examen.append(calificaciones[i][0])
      #Si la calificacion es menor a 3.0, se agrega el nombre a la lista de reprobados
      elif calificaciones[i][1] < 3.0:
            reprobados.append(calificaciones[i][0])
      #Aumentamos el contador para que se continue recorriendo la lista 
      i+=1
#Recorremos la lista por segunda vez para obtener una lista con todas las notas
while mi < len(calificaciones):
      notas.append(calificaciones[mi][1])
      mi += 1
#Obtenemos la nota maxima del listado de notas
maximo = max(notas)
#Recorremos la lista de calificaciones por tercera vez para obtener el nombre
#de la persona que obtuvo la mejor nota y asi agregar el nombre y la nota a la lista
#de mejor nota
while ma <len(calificaciones):
      if maximo == calificaciones[ma][1]:
            mejor.append(calificaciones[ma])
      ma+=1
#Obtenemos la peor nota del listado de notas
minimo = min(notas)
#Recorremos la lista de calificaciones por cuarta vez para obtener el nombre
#de la persona que obtuvo la peor nota y asi agregar el nombre y la nota a la lista
#de peor nota
while me < len(calificaciones):
      if minimo == calificaciones[me][1]:
            peor.append(calificaciones[me])
      me+=1
#Calculamos el promedio de todas las notas
promedio = sum(notas)/len(notas)
#Recorremos la lista por ultima vez
while final < len(calificaciones):
      #Si la nota ingresa es invalida (no es nota o no esta entre 0 y 7.0, ambos includos
      if calificaciones[final][1] < 0.0 or calificaciones[final][1] > 7.0:
            #Flag cambiara a ser falso y se rompe el ciclo while
            flag = False
            break
      else:
            #De lo contrario, se sigue recorriendo para asegurar que todas las notas sean validas
            final+=1
#SALIDA
#Si flag es True, entonces el programa devuelve las listas solicitadas
if flag == True:      
      print("La lista de alumnos reprobados es:", reprobados)
      print("La lista de alumnos que rinden examen es:", examen)
      print("La lista de alumnos aprobados es:",aprobados)
      print("La peor calificaciones es:",peor)
      print("La mejor calificacion es:", mejor)
      print("El promedio de calificaciones es:", promedio)
else:
      #De lo contrario, entonces el programa le pide al usuario que ingrese una nota valida esta vez.
      print("Debe ingresar notas validas, las cuales deben estar entre 0.0 y 7.0, ambos incluidos.")
      print("Intentelo denuevo")
