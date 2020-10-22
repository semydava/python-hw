def sort_letters(text):
    """
    Return a string of the same letters where all the letters are sorted by
    its frequency in descending order. In case of equal frequency letters
    should go in the order they were met in the original string.
    >>> sort_letters('aaabccccdeefffff')
    'fffffccccaaaeebd'
    >>> sort_letters('abcdefghijklmnop')
    'abcdefghijklmnop'
    >>> sort_letters('')
    ''
    >>> sort_letters('aba')
    'aab'
    >>> sort_letters('abcabccba')
    'aaabbbccc'
    """
    letters_by_numbers = {}
    sorted_text = ''
    for char in text:
      key = char 
      value = text.count(char)
      letters_by_numbers[key] = value
    letters_by_numbers_list = list(letters_by_numbers.items())
    letters_by_numbers_list.sort(key=lambda i: i[1], reverse = True)
    for pair in letters_by_numbers_list:
      letters = pair[0] * pair[1]
      sorted_text+=letters
    return sorted_text
print(sort_letters('aaddbbbccc'))