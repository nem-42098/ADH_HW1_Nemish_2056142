import numpy



n,m=input().split(' ')
list1=[]
for _ in range(int(n)):
    list1.append(input().split(' '))
arr1=numpy.array(list1,int)
print(numpy.mean(arr1,axis=1))
print(numpy.var(arr1,axis=0))
print(round(numpy.std(arr1),11))
