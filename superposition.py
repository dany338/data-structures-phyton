def superposition(list1, list2):
  for elem in list1:
    if elem in list2:
      return True
  return False

print("superposition")
print(superposition([1,2,3],[7,4,5]))