def generator_n_charaters(charater,n):
  string = charater
  for i in range(0,n+1):
    string += charater
  return string

print("generator_n_charaters")
print(generator_n_charaters("a",5))
print(generator_n_charaters("b",3))
print(generator_n_charaters("c",4))
print(generator_n_charaters("d",2))

def generator_n_charaters_two(charater,n):
  return charater * n