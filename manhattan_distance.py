def manhattan_distance(pointA, pointB):
  i = 0
  distance = 0
  while i < len(pointA):
    length_projections = abs(pointA[i] - pointB[i])
    distance += length_projections
    i += 1
  return distance