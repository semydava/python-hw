#https://github.com/inesusvet/pyclub/blob/master/problems/open_and_close.py
def is_balanced(text,caps):
  """
  >>> is_balanced('')
  True
  >>> is_balanced('Sensei says yes!')
  True
  >>> is_balanced('))((')
  False
  >>> is_balanced('"')
  False
  >>> is_balanced("[('''Sensei says yes!)]")
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
  possible_brackets ={}
  for i, char in enumerate(caps):
    if i %2 ==0:
      key = char
    else:
      value = char
      possible_brackets[key] = value
  print(possible_brackets)
  brackets =[]
  brackets_stack = []


  if len(text) == 0:
    return True 

  for char in text:
    if char in possible_brackets.keys() or char in possible_brackets.values():
      brackets.append(char)
  print(brackets)

  for element in brackets:
    if element in possible_brackets and element in possible_brackets.values():
      if brackets.count(element)%2 == 0:
          pass
      else:
          brackets_stack.append(element)

    elif element in possible_brackets:
      brackets_stack.append(element)
    else:
      if len(brackets_stack)==0:
        return False
      current_char = brackets_stack.pop()
      
      if element != possible_brackets[current_char]:
          return False


  return not brackets_stack 

  
  
print(is_balanced("abcd-e@fghi@", "--@@"))