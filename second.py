# Implementar una función llamada encontrarFrases en NodeJs que
# reciba como primer parámetro un texto y como segundo parámetro
# un arreglo de textos y devuelva un arreglo de los
# textos que pueden ser construidos a partir de los
# caracteres de los textos del primer parámetro.

# Por ejemplo si la función se invoca de esta manera:
# const resultado = encontrarFrases("Yo soy un developer", [
# "Yo puedo",
# "Yo puedo puedo",
# "No coincide",
# "pelo duro",
# ]);
### trie, prefix-trees
# el resultado deberá contener 2 elementos ["pelo duro", "Yo puedo"] ya que
# ambas frases se pueden construir utilizando los caracteres del texto
# "Yo soy un developer" sin reutilizar letras.

# Considera que tanto los textos como las frases pueden tener hasta 1,000,000
# de caracteres por lo que tu código deberá ser lo más eficiente posible.

def test(counter, target):
  # sentence: "Yo soy un developer"
  # target: "pelo duro"
  for c in target:
    if c in counter:
      counter[c] -= 1
      if counter[c] < 0:
        return False
    else:
      return False
  return True

def pre_process(sentence):
  counter = {}
  for c in sentence:
    if c not in counter:
      counter[c] = 0
    counter[c] += 1
  return counter

# b = len(w)
# c = max( len ( arr[i] ))
# n = len(arr)
# runtime complexity: O(b + c*n) las expressiones regulares son buenas para resolver estos problemas
# siempre y cuando haya un mismo patron
def find_strs(w, arr):
  result = []
  counter = pre_process(w) # O(b)

  # O(c*n)
  for c in arr: # O(n)
    if test(counter.copy(), c): # O(c)
      result.append(c)
  return result

print(find_strs("Yo soy un developer", ["Yo puedo", "Yo puedo puedo", "No coincide", "pelo duro"]))
