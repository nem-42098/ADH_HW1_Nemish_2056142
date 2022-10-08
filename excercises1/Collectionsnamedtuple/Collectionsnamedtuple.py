# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
Student=namedtuple('Student','ID, MARKS, CLASS, NAME')
n_student=int(input())
l=input().split()
sum1=0
j=l.index('MARKS')
for i in range(n_student):
    sum1=sum1+int(input().split()[j])
print(sum1/n_student)
