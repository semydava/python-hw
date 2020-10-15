def countSort(A):
  C=[]
  for i in range(100):
    C+=[0]
  for i in A:
    C[i]+=1
  j=0
  for i in range(100):
    if C[i]>0:
      A[j]=i
      j+=1
  return A

print(countSort([56,67,1,2,3,45,23,90,17]))