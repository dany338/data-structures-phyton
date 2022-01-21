def inverse(cadena):
  longitude = -(len(cadena)-1)
  new_cadena = str()
  for n in range(longitude,1):
    n = abs(n)
    new_cadena += cadena[n]
  return new_cadena

def is_palyndrome(cadena):
  new_cadena = inverse(cadena)
  if cadena == new_cadena:
    return True

print(is_palyndrome("hola"))
print(is_palyndrome("amor"))
print(is_palyndrome("oso"))
print(is_palyndrome("ana"))