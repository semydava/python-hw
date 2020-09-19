#https://github.com/inesusvet/pyclub/blob/master/problems/reverse_words.py
def reverse_words(text):
  separate_words = text.split()
  reverse_words = ''
  for char in separate_words:
    reversed_word = char[::-1]
    reverse_words = reverse_words + reversed_word + ' '
    if separate_words.index(char) == len(separate_words)-1:
      reverse_words = reverse_words + reversed_word

  return reverse_words