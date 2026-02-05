def calorias(tipo_ejercicio, minutos):
      if tipo_ejercicio == 'Correr':
            if minutos >= 21:
                  a = 20* 10
                  b = minutos - 20
                  c = b * 12
                  d = a + c
                  return d
            else:
                  return minutos * 10
      elif tipo_ejercicio == 'Bicicleta':
            if minutos >= 21:
                  a = 20 * 4
                  b = minutos - 20
                  c = b * 5
                  d = a + c
                  return d
            else:
                  return minutos * 4
      elif tipo_ejercicio == 'Natacion':
            if minutos >= 21:
                  a = 20 * 7
                  b = minutos - 20
                  c = b * 8
                  d = a + c
                  return d
            else:
                  return minutos * 7
      else:
            return 0
print(calorias('Correr', 45))
print(calorias('Natacion', 10))
print(calorias('Pesas', 20))
                               
