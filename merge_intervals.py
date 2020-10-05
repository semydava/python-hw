#https://github.com/inesusvet/pyclub/blob/master/problems/merge_intervals.py
def merge(intervals):
  """
  See https://leetcode.com/problems/merge-intervals/
  >>> merge([[1, 3], [2, 6], [8, 10], [15, 18]])
  [[1, 6], [8, 10], [15, 18]]
  >>> merge([[1, 4], [4, 5]])
  [[1, 5]]
  >>> merge([[1, 2], [3, 5]])
  [[1, 2],[3,5]] 
  >>> merge([[3,8],[7,10]])
  [[3, 10]]
  >>> merge([[1,4],[2,3]])
  [[1, 4]]
  """
  intervals.sort()
  intervals_stack = []
  for pair in intervals:
    if len(intervals_stack) == 0:
      intervals_stack.append(pair)
    else:
      current_pair = intervals_stack[len(intervals_stack)-1]
      if current_pair[1]>=pair[0]:
        if current_pair[1]<pair[1]:
          new_pair = [current_pair[0],pair[1]]
          intervals_stack.remove(current_pair)
          intervals_stack.append(new_pair)
        else:
          new_pair = [current_pair[0],current_pair[1]]
          intervals_stack.remove(current_pair)
          intervals_stack.append(new_pair)

      else:
        intervals_stack.append(pair)       
  return intervals_stack
  
print(merge([[1,4],[2,3]]))