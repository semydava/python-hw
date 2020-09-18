https://www.codewars.com/kata/52998bf8caa22d98b800003a
def manhattan_distance(pointA, pointB):
  distance = 0
  for (element1,element2) in zip(pointA,pointB):
    length_projections = abs(element1 - element2)
    distance += length_projections
  return distance