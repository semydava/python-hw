def findContentChildren(greed, sizes):
    """
    >>> findContentChildren([1,2,3], [1,1])
    1
    >>> findContentChildren([1,2], [1,2,3])
    2
    >>> findContentChildren(list(range(1, 11)), [1] * 100 + list(range(1, 11)))
    10
    >>> findContentChildren([2, 3, 4, 2], [1, 1, 1, 1])
    0
    >>> findContentChildren([1, 2, 3, 4, 5], [5, 5, 3, 3, 1])
    5
    >>> findContentChildren([1, 2, 3, 4, 5], [])
    0
    >>> findContentChildren([1,100500000000], [2,10])
    1
    """
    greed, sizes = sorted(greed), sorted(sizes)
    finalContent = 0
    i = j = 0
    if len(sizes) == 0 or len(greed) == 0:
      return 0
    while i < len(greed) and j < len(sizes):
      if sizes[j] >= greed[i]:
        finalContent += 1
        j+=1
        i+=1
      else:
        j+=1

    return finalContent
  
