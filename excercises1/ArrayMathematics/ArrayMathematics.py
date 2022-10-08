import numpy


n,m=input().split(' ')
list1=[]
for i in range(int(n)):
    list1.append(input().split(' '))
arr1=numpy.array(list1,int)

list2=[]
for i in range(int(n)):
    list2.append(input().split(' '))
arr2=numpy.array(list2,int)
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(numpy.floor_divide(arr1,arr2))
print(arr1%arr2)
print(arr1**arr2)
