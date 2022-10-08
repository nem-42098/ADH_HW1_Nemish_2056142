# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
N_shoes=int(input())
size=list(map(int,input().split()))
c1=Counter(size)
N_customer=int(input())
earned=0
for i in range(N_customer):
    custom=list(map(int,input().split()))
    
    
    if (custom[0] in set(size)) and (c1[custom[0]]>0):
        earned=earned+custom[1]
        c1[custom[0]]=c1[custom[0]]-1
print(earned)
