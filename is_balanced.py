#https://github.com/inesusvet/pyclub/blob/master/problems/open_and_close.py
def is_balanced(text):
  """
  >>> is_balanced('')
  True
  >>> is_balanced('Sensei says yes!')
  True
  >>> is_balanced('))((')
  False
  >>> is_balanced('(Sensei says yes!)')
  True
  >>> is_balanced('(Sensei says no!')
  False
  >>> is_balanced('[Sensei] (says) {yes!}')
  True
  >>> is_balanced('{Sensei (says) yes!}')
  True
  >>> is_balanced('[(Sensei) says) no!)')
  False
  >>> is_balanced('(Sensei (says) (yes!))')
  True
  """
  possible_brackets = {'(':')','[':']','{':'}'}
  brackets =[]
  brackets_stack = []

  if len(text) == 0:
    return True 

  for char in text:
    if char in possible_brackets.keys() or char in possible_brackets.values():
      brackets.append(char)
  

  for element in brackets:
    if element in possible_brackets.keys():
      brackets_stack.append(element)
    else:
      if len(brackets_stack)==0:
        return False
      current_char = brackets_stack.pop()
      
      if current_char == possible_brackets.keys():
        if element != possible_brackets.values():
          return False
        

  return not brackets_stack

  
  
print(is_balanced('(Sensei (says) (yes!))'))