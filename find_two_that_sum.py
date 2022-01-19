# 9 - 2 = 7
# 9 - 7 = 2
# 9 - 11 = -2
# 9 - -2 = 11

# runtime complexity: amortized cost:
# expected runtime complexity O(n) ?
def find_two_than_sum_1(arr, target):
  n = len(arr)
  c = {}
  for i in range(n):  # O(n) ?
    c[target - arr[i]] = i # amortized cost: O(1) ?
  result = []
  for i in range(n):  # O(n) ?
    if arr[i] in c:  # amortized cost: O(1) ? --> c.find(arr[i]) -->hash_table ? --> O(1)
      return (i, c[arr[i]])  # O(1) ?
  return result

print(find_two_than_sum_1( [2, 7, 11, -2], target = 9))

# runtime complexity: O(n) ? bitset array set, indexar los elementos su costo es O(1)
def find_two_than_sum_2(arr, target):
  n = len(arr)
  c = {}
  for i in range(n):  # O(n) ?
    c[target - arr[i]] = i # amortized cost: O(1) ?
  result = []
  for i in range(n):  # O(n) ?
    if arr[i] in c:  # amortized cost: O(1) ? --> c.find(arr[i]) -->hash_table ? --> O(1)
      return (i, c[arr[i]])  # O(1) ?
  return result

print(find_two_than_sum_2( [2, 7, 11, -2], target = 9))
