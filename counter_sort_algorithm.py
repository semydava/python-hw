def countSort(A):
  h = max(A) + 1 
  l = min(A)
  d = (h - l)
  C=[0]*d
  sorted_numbers = []
  for n in A: 
    j = n-l
    C[j] += 1
  for i in range(d):
    if C[i] > 0:
      value = [i+l] * C[i]
      sorted_numbers.extend(value)

  return sorted_numbers
print(countSort([-2, 1, 4, -3, 5]))