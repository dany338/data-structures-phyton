def inverse(cadena):
    cadena = cadena[::-1]
    return cadena

print(inverse("hola"))

def inverse_two(cadena):
  longitude = -(len(cadena)-1)
  new_cadena = str()
  for n in range(longitude,1):
    n = abs(n)
    new_cadena += cadena[n]
  return new_cadena

print(inverse_two("hola"))