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
