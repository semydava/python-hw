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
    possible_brackets = ['(',')','[',']','{','}']
    opening_brackets = ['(','{','[']
    brackets =[]
    brackets_stack = []
    i = 0 
    if len(text) == 0:
      return True 

    for char in text:
      if char in possible_brackets:
        brackets.append(char)
    

    for i in range(len(brackets)):
      element = brackets[i]
      
     
      if element in opening_brackets:
        brackets_stack.append(element)

      else:
        if len(brackets_stack)==0:
          return False
      
        current_char = brackets_stack.pop()

        if current_char == '(':
          if element != ')':
            return False
          
       
        if current_char == '{':
          if element != '}':
            return False 
        

        if current_char == '[':
          if element != ']':
            return False 

      i+=1

    if len(brackets_stack) != 0:
      return False
    return True

  
  
print(is_balanced('][({fff})]hasattr'))