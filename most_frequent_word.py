#https://github.com/inesusvet/pyclub/blob/master/problems/most_frequent_word.py
def most_frequent_word(text):
    """
    >>> most_frequent_word('i think therefore i am')
    'i'
    >>> most_frequent_word("be the change that you wish to see in the world")
    'the'

    """
    number_repeat = {}
    text = text.split()
    for char in text:
        if char not in number_repeat:
            number_repeat[char] = 0
        number_repeat[char] += 1
      #number = text.count(char)  
      #number_repeat[char] = number
    if number_repeat: 
      maximum = max(number_repeat.values())
      for key, value in number_repeat.items():
        if value == maximum:
          return key 
   print(most_frequent_word('He is is hardworking man'))