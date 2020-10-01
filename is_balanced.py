#https://github.com/inesusvet/pyclub/blob/master/problems/open_and_close.py
def is_balanced(text):
  """
  >>> is_balanced('')
  True
  >>> is_balanced('Sensei says yes!')
  True
  >>> is_balanced('))((')
  False
  >>> is_balanced('(]')
  False
  >>> is_balanced('[()[]]')
  True
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
    if element in possible_brackets:
      brackets_stack.append(element)
     
    else:
      if len(brackets_stack)==0:
        return False
      current_char = brackets_stack.pop()
      
      if element != possible_brackets[current_char]:
          return False
        

  return not brackets_stack

  
  
print(is_balanced('(Sensei says yes!)'))