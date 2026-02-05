'''Cual es la salida correcta?'''
a = 3
b = 7
c = 9
result = a * b + c
if ((a-3) == 0) or ((b %3) == 0) or ((c/9) == 1):
    result = result -2
if ((a%2) == 1) and ((b%2) == 1) and  ((c%2) == 1):
    result = result * 2
if ((a%2) == 0) and ((b%7) == 0) and ((c % 9) == 0):
    result = result * -1
if ((a // True) == 3) or ((b-3) == 5) or ((c + False) == 9):
    result = result + 4

print(result)
    

