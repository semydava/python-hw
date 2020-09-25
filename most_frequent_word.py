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
      number = text.count(char) 
      if number > 1: 
        number_repeat[char] = number
    maximum = max(number_repeat.values())
    for key, value in number_repeat.items():
      if value == maximum:
        return key 
