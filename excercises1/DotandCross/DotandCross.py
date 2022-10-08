import numpy

n=input()
list1=[]
for _ in range(int(n)):
    list1.append(input().split(' '))
arr1=numpy.array(list1,int)
list1=[]
for _ in range(int(n)):
    list1.append(input().split(' '))
arr2=numpy.array(list1,int)
print(numpy.matmul(arr1,arr2))
