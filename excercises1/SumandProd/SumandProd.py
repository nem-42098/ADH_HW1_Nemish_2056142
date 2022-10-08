import numpy

m,n=input().split(' ')
list1=[]
for _ in range(int(n)):
    list1.append(input().split(' '))
arr1=numpy.array(list1,int)
#print(numpy.sum(arr1,axis=0))
print(numpy.product(numpy.sum(arr1,axis=0),axis=0))
    

