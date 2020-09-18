def max_and_min(arr1,arr2):
  arr1.sort()
  arr2.sort()
  difference = []

  for element1 in arr1:
    local = []
    for element2 in arr2 :
      local_dif = abs(element1 - element2)
      local.append(local_dif)
    local.sort()  
    difference.append(min(local))
    difference.append(max(local))

    
  difference.sort()
  maximum = max(difference)
  minimum = min(difference)
  return [maximum,minimum]