#https://www.codewars.com/kata/58902f676f4873338700011f/python
def is_lucky(ticket):
    first_digits = ticket [:3]
    last_digits = ticket[3:]

    
    sum_first_digits = 0
    sum_last_digits = 0

    if len(ticket) != 6:
      return False

    for (char1,char2) in zip(first_digits,last_digits):
      if not char1.isdigit() or not char2.isdigit():
        return False

      sum_first_digits += int(char1)
      sum_last_digits += int(char2)
      

    return sum_last_digits == sum_first_digits
