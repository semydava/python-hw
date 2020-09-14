def wave(people):
  wave_result = []
  for i in range (0,len(people)):
    if people[i] == ' ':
      continue
    new_char = people[i].upper()
    people = people[:i] + new_char + people[i+1:]
    wave_result.append(people) 
    people = people.lower()
  return wave_result

print(wave('two words'))
    