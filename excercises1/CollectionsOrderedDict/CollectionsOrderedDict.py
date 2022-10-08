# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n_items=int(input())
od=OrderedDict()
for i in range(n_items):
    m=input().split()
    if str(' '.join(m[0:-1])) in set(od.keys()):
        od[' '.join(m[0:-1])]=od[' '.join(m[0:-1])]+int(m[-1])
    else:
        od[' '.join(m[0:-1])]=int(m[-1])
for j in od:
    print(j,od[j])
