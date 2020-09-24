#https://www.codewars.com/kata/59377c53e66267c8f6000027/solutions/python
def alphabet_war(fight):
   """
    >>> alphabet_war('')
    "Let's fight again!"
    >>> alphabet_war('abracadabra')
    'Left side wins!'
    >>> alphabet_war('z')
    'Right side wins!'
    >>> alphabet_war('zdqmwpbs')
    "Let's fight again!"
    >>> alphabet_war('zzzzs')
    'Right side wins!'
    >>> alphabet_war('wwwwwwz')
    'Left side wins!'
  """
  left_letters = {'w':4, 'p':3, 'b':2,'s':1}
  right_letters = {'m':4, 'q':3,'d':2, 'z':1}
  sum_left = 0
  sum_right = 0
  fight =  fight.lower()
  for char in fight:
    if char in left_letters:
      number1 = left_letters[char]
      sum_left += number1
          
    elif char in right_letters:
      number2 = right_letters[char]
      sum_right += number2 
  if sum_left > sum_right:
    return "Left side wins!"
  elif sum_right > sum_left: 
    return "Right side wins!"
  else:
    return "Let's fight again!"
 
