import numpy


list1=[]
for _ in range(int(input())):
    list1.append(input().split(' '))
arr1=numpy.array(list1,dtype=float)
y=numpy.linalg.det(arr1)
i=str(y).find('.')
if len(str(y)[i:-1])>2:
    print('{:.2f}'.format(y))
else:
    print('{:.1f}'.format(y))
