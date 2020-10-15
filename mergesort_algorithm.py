def mergesort(text):
  if len(text) > 1:
    middle = len(text) // 2
    left_part = text[:middle]
    right_part = text[middle:]
    i = 0
    j = 0
    k = 0
    mergesort(left_part)
    mergesort(right_part)
    while i < len(left_part) and j < len(right_part):
      if left_part[i] < right_part[j]:
        text[k] = left_part[i]
        i+=1
      else:
        text[k] = right_part[j]
        j+=1
      k+=1
    while i < len(left_part):
      text[k] = left_part[i]
      i+=1
      k+=1  
    while j < len(right_part):
      text[k] = right_part[j]
      j+=1
      k+=1
  return text
      


print(mergesort([54]))