#https://www.codewars.com/kata/5648b12ce68d9daa6b000099
def number(bus_stops):
  left_people = 0 
 
  for char in bus_stops:
    in_people = char[0]
    out_people = char[1]
    left_people += in_people - out_people  
    
     
  return left_people

t = [[10,0],[3,5],[5,8]]
a = [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]
k = [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]
e = [[0,0]]
print(number(t))
print(number(a))
print(number(k))
print(number(e))