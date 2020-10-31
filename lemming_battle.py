def is_alive(power):
    """
    Отвечает на вопрос: жив ли лемминг?
    >>> is_alive(0)
    False
    >>> is_alive(100)
    True
    >>> is_alive(-10)
    False
    """
    if power <= 0:
      return False
    return True

def triage(warriors):
    """
    Отбирает только выживших леммингов после раунда боев.
    >>> triage([10, 0, 5, -2])
    [10, 5]
    """
    alive_warriors = []
    for power in warriors:
      if is_alive(power):
        alive_warriors.append(power)

    return alive_warriors


def fight(green, blue):
    """
    Отвечает на вопрос: сколько силы останется у двух леммингов после их боя?
    >>> fight(10, 10)
    (0, 0)
    >>> fight(12, 10)
    (2, -2) 
    >>> fight(10, 15)
    (-5, 5)
    """
    left_power = []
    left_power.append(green - blue)
    left_power.append(blue - green)
    return tuple(left_power)


def round(green, blue):
    """
    Проводит раунд боев между двумя группами леммингов.
    Количество элементов в каждой группе всегда одинаковое.
    >>> round([1, 2, 3], [3, 2, 1])
    [(-2, 0, 2), (2, 0, -2)]
    >>> round([10], [5])
    [(5,), (-5,)]
    """
    round_result = []
    green_round = []
    blue_round = []
    for (green_power,blue_power) in zip(green,blue):
      current_round = (fight(green_power,blue_power))
      green_round.append(current_round[0])
      blue_round.append(current_round[1])
  
    round_result.append(tuple(green_round))
    round_result.append(tuple(blue_round))
    return round_result
#print(round([10], [5]))



def draw(army, size):
    """
    Выбирает из армии нескольких самых сильных леммингов.
    >>> draw([1, 2, 3, 4, 5], 3)
    [5, 4, 3]
    >>> draw([10, 1, 2], 2)
    [10, 2]
    >>> draw([1, 10, 2], 1)
    [10]
    """
    army.sort(reverse = True)
    strong_army =[]
    if len(army) >= size:
      for i in range(size):
        strong_army.append(army[i])
      return strong_army
    return False
#print(draw([1, 2, 3], 3))


def collect(army, warriors):
    """
    Возвращает в армию леммингов, выживших после раунда боев.
    >>> collect([], [1, 2, 3])
    [1, 2, 3]
    >>> collect([10, 9, 8, 7], [1, 2, 3])
    [10, 9, 8, 7, 1, 2, 3]
    """ 
    army.extend(warriors)
    return army



def lemming_battle(battlefield, green, blue):
    """
    Проводит войну между двумя армиями леммингов на заданном количестве полей.
    """
    green_strong = draw(green, battlefield)
    blue_strong = draw(blue,battlefield)
    green_round = []
    blue_round = []
    green_alived = []
    blue_alived = []
    g =0
    b=0
    while g < len(green_strong) and b < len(blue_strong):
        green.remove(green_strong[g])
        blue.remove(blue_strong[b])
        g+=1
        b+=1
    round_result = round(green_strong,blue_strong)
    green_round.extend(list(round_result[0]))
    blue_round.extend(list(round_result[1]))
    green_alived = triage(green_round)
    blue_alived = triage(blue_round)
    green = collect(green,green_alived)
    blue = collect(blue,blue_alived)
    green_strong.clear()
    blue_strong.clear()
    green_round.clear()
    blue_round.clear()
    green_alived.clear()
    blue_alived.clear()
    if len(green) == 0 and len(blue) == 0:
      return 'Green and Blue died'
    else:
      if len(green) != 0 and len(blue) != 0:
        if len(green) < len(blue):
          green_strong = draw(green,len(green))
          blue_strong = draw(blue,len(green))
          while g < len(green_strong) and b < len(blue_strong):
            green.remove(green_strong[g])
            blue.remove(blue_strong[b])
            g+=1
            b+=1
          round_result = round(green_strong,blue_strong)
          green_round.extend(list(round_result[0]))
          blue_round.extend(list(round_result[1]))
          green_alived = triage(green_round)
          blue_alived = triage(blue_round)
          green = collect(green,green_alived)
          blue = collect(blue,blue_alived)

        else:
          green_strong = draw(green,len(blue))
          blue_strong = draw(blue,len(blue))
          while g < len(green_strong) and b < len(blue_strong):
            print(green_strong[g])
            green.remove(green_strong[g])
            blue.remove(blue_strong[b])
            g+=1
            b+=1
          print(green,blue)
          round_result = round(green_strong,blue_strong)
          green_round.extend(list(round_result[0]))
          blue_round.extend(list(round_result[1]))
          green_alived = triage(green_round)
          blue_alived = triage(blue_round)
          green = collect(green,green_alived)
          blue = collect(blue,blue_alived)
          print(green,blue)


      elif len(blue) == 0 and len(green) != 0:
        return 'Green wins'
      elif len(green) == 0 and len(blue) != 0:
        return 'Blue wins' 
    
  
print(lemming_battle(2, [15, 5], [15, 5, 5]))

    





    



