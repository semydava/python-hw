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
    return power > 0 
  

def triage(warriors):
    """
    Отбирает только выживших леммингов после раунда боев.
    >>> triage([10, 0, 5, -2])
    [10, 5]
    """
    # list comprehension
    alive_warriors = [power for power in warriors if is_alive(power)]
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
    return green - blue, blue - green


def round(green, blue):
    """
    Проводит раунд боев между двумя группами леммингов.
    Количество элементов в каждой группе всегда одинаковое.
    >>> round([1, 2, 3], [3, 2, 1])
    [(-2, 0, 2), (2, 0, -2)]
    >>> round([10], [5])
    [(5,), (-5,)]
    """
    # list comprehension 
    current_round = [fight(green_power,blue_power) for (green_power,blue_power) in zip(green,blue)]
    green_round = [i[0] for i in current_round]
    blue_round = [i[1] for i in current_round]
    return tuple(green_round), tuple(blue_round)




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
    army.sort(reverse = True)#O(nlog(n))
    return army[:size]
  


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
    while len(green)>0 and len(blue)>0:#O(n)
      size = min([battlefield,len(green),len(blue)])#O(1)
      g = draw(green, size)#O(nlog(n))
      b = draw(blue,size)#O(nlog(n))
      green = green[len(g):]#O(1)
      blue = blue[len(b):]
      g,b = round(g,b)#O(size)
      g = triage(g)#O(k)
      b = triage(b)
      collect(green,g)
      collect(blue,b)
      green.sort(reverse = True)
      blue.sort(reverse = True)
    if len(blue) == 0 and len(green) != 0: 
      result = 'Green wins: ' + ' '.join(str(i) for i in green)
    elif len(green) == 0 and len(blue) != 0:
      result = 'Blue wins: ' + ' '.join(str(i) for i in blue)
    else:
      result = 'Green and Blue died'  
    #O(n) * (O(nlogn) + nlogn + k +k) = O(n) * O(nlogn)=nˆ2logn
    return result 

print(lemming_battle(10, [49], [825, 322, 981, 697, 564, 384]))




