#https://www.codewars.com/kata/58902f676f4873338700011f/python
def is_lucky(ticket):
    first_digits = ticket [:3]
    last_digits = ticket[3:]

    i = 0
    sum_first_digits = 0
    sum_last_digits = 0

    if len(ticket) != 6:
      return False

    while i < len(first_digits) and i < len(last_digits):
      if not first_digits[i].isdigit() or not last_digits[i].isdigit():
        return False

      sum_first_digits += int(first_digits[i])
      sum_last_digits += int(last_digits[i])
      i +=1

    return sum_last_digits == sum_first_digits