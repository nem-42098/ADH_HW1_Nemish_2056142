# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
result=input().split(' ')

print(numpy.zeros(tuple([int(x) for x in result]),dtype=numpy.int))
print(numpy.ones(tuple([int(x) for x in result]),dtype=numpy.int))
