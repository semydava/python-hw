def revert_vovels(text):
  vovels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U','u']
  vovels_in_text = ''
  strs = ''
 
  for char in text:
    if char in vovels:
      vovels_in_text += char
  reversed_vovels_in_text = vovels_in_text[::-1] 

  print(reversed_vovels_in_text)
  index = 0
  for element in text:
    if element in vovels_in_text:
      strs += reversed_vovels_in_text[index]
      index += 1
    else: 
      strs += element

  return strs