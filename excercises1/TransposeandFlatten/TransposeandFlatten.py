import numpy


result=[]

n,m=input().split(' ')

for _ in range(int(n)):
  
    result.append(input().split(' '))
arr=numpy.array(result,int)
print(arr.T)
print(arr.flatten())
