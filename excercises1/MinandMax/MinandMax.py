import numpy



n,m=input().split(' ')
list1=[]
for _ in range(int(n)):
    list1.append(input().split(' '))
arr1=numpy.array(list1,int)
print(numpy.max(numpy.min(arr1,axis=1)))
