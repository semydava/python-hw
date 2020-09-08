def number(bus_stops):
  left_people = 0 
  index = 0
  length = len(bus_stops)
  while index < length:
    current_stop = bus_stops[index]
    in_people = current_stop[0]
    out_people = current_stop[1]

    #check whether input is correct 
    if index == 0 and current_stop[1] != 0:
      return 0
    
    left_people += in_people - out_people 
    index+=1
  return left_people


  
t = [[10,0],[3,5],[5,8]]
a = [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]
k = [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]
e = [[0,0]]
print(number(t))
print(number(a))
print(number(k))
print(number(e))

  