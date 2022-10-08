# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
m,n=map(int,input().split())
d=defaultdict(list)
for i in range(m):
    d[input()].append(i+1)   


for j in range(n):
    k=input()
    if k in set(d.keys()):
        print(*d[k])
    else:
        print(-1)
