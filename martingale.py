#https://www.codewars.com/kata/5eb34624fec7d10016de426e/python
def martingale(bank, outcomes):
  stake = 100
  
  for char in outcomes:
    if char == 1:
      bank += stake
      stake = 100
    else: 
      bank -= stake
      stake *= 2  
   
  return bank 
