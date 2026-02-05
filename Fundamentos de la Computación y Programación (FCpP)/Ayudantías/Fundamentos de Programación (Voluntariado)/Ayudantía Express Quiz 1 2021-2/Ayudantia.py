# MEGA RESUMEN DE LA AYUDANTIA
# Tipos de datos y expresiones matematicas
'''
CONSOLA: NOS PERMITE REALIZAR OPERACIONES RAPIDAS O
COMPROBAR OPERACIONES.

int = 4 , 28 1000 300000
float = 40.0 28.7 388.667
str string = 'hola' 'perrito' 'ayudantia'
booleanos bool = True False
True = 1.0 o 1
False = 0 o 0.0

TRANSFORMACIONES DE DATOS
entero
int()

floatante
float()

string
str()

booleano
bool()

PARA LA OPERACIÓN MODULO ( O RESTO) (%):
primero: se dividen ambos numeros
segundo: verifico si son de signos iguales
tercero: si son distintos, le sumo 1 a la parte entera
del resultado. Multiplico el 2do numero con el resultado
cuarto: verifico lo que me falta para llegar al primer numero
EJEMPLOS:
20%3 -> 3*6 = 18 +2  MISMO SIGNO
-20%-3 -> -3 * 6 = -18 -2   MISMO SIGNO
-20%3 -> 3*-(6+1) = -21+1 = -20  DISTINTO SIGNO

OPERACIONES
suma y resta
2+3 2-3  (FLOTANTE + ENTERO = FLOTANTE)
multiplicacion
2*3
division normal
2/3 -> flotante
division entera
2//3 -> entero
2**3
2%3

# Estructura de Scripting

strings:
+: Concatena strings (los une)
*: repite cosas, respetando como esta escrito

nombre = "2" + "hola" = "2hola"
nombre = "hola "*2 = "holahola"
print: Imprime cosas, puedo colocar variables dentro
input("Coloque su edad: ")-> string

edad = int(input("Coloque su edad: ")) -> ENTERO
print(type(edad))

COMPARACIONES
== : Igual
>
<
>= : Mayor o igual
<= : Menor o igual
!= : Signo de diferencia (o distinto)

and : Y (logica)-> Si ambos son verdaderos = True
or: o (logica) -> Solamente da falso si ambos son falsos

# Decisiones
numero = 0
CADA IF ES UN BLOQUE!

if numero == 1:
    condiciones
elif (opcional):
    condiciones
else(opcional):

if ((numero +0) == 0):
    condiciones

SI SE TIENEN MULTIPLES IFS SEGUIDOS, AUNQUE SE EJECUTE
EL PRIMERO, PYTHON IGUAL VERIFICARÁ EL SEGUNDO Y LOS DEMAS!
UN IF PUEDE IR SIN UN ELSE!
'''



    










      
