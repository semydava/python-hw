def split(input_data):
  middle = len(input_data) // 2
  left_part = input_data[:middle]
  right_part = input_data[middle:]
  return left_part, right_part

def merge_list(left_part,right_part):
  sorted_text = []
  i = 0
  j = 0
  if len(left_part) == 0:
    return right_part
  if len(right_part) == 0:
    return left_part
  while len(sorted_text) < (len(left_part) + len(right_part)):
    if left_part[i] < right_part[j]:
      sorted_text.append(left_part[i])
      i+=1
    else:
      sorted_text.append(right_part[j])
      j+=1
    if i == len(left_part):
      sorted_text+=right_part[j:]
      break
    elif j == len(right_part):
      sorted_text+=left_part[i:]
      break
  return sorted_text

def mergesort(input_data):
  if len(input_data) <= 1:
    return input_data
  else:
    left_part,right_part = split(input_data)
    return merge_list(mergesort(left_part),mergesort(right_part))