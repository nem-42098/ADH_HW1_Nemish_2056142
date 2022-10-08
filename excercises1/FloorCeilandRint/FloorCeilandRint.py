import numpy
numpy.set_printoptions(legacy='1.13')

m=input().split(' ')
arr1=numpy.array(m,float)
print(numpy.floor(arr1))
print(numpy.ceil(arr1))
print(numpy.rint(arr1))
