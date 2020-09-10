#https://www.codewars.com/kata/5eb34624fec7d10016de426e/python
def martingale(bank, outcomes):
  stake = 100
  i = 0

  while i < len(outcomes):
    if outcomes[i] == 1:
      bank += stake
      stake = 100
    else: 
      bank -= stake
      stake *= 2  
    i += 1
  return bank 
