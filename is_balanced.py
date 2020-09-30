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
    >>> is_balanced('(Sensei) (says) (yes!)')
    True
    >>> is_balanced('(Sensei (says) yes!)')
    True
    >>> is_balanced('((Sensei) says) no!)')
    False
    >>> is_balanced('(Sensei (says) (yes!))')
    True
    """
    brackets =[]
    brackets_stack = []
    i = 0 
    if len(text) == 0:
      return True 

    if text.count(')') != text.count('('):
      return False

    for char in text:
      if char == '(' or char == ')':
        brackets.append(char)
    
    

    for i in range(len(brackets)):
      element = brackets[i]
      
      if element == '(':
        brackets_stack.append(element)
        
      else:
        if len(brackets_stack)==0:
          return False
        current_char = brackets_stack.pop()
        
        if current_char == '(':
          
          if char != ')':
            return False
      i+=1
    if len(brackets_stack) != 0:
      return False
    return True

  
  
print(is_balanced(')(Sensei (says) yes!)('))