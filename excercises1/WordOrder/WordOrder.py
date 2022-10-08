# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
M=int(input())
od=OrderedDict()
for i in range(M):
    m=input()
    if m in od.keys():
        od[m]=od[m]+1
    else:
        od[m]=1
print(len(od.keys()))
print(*od.values())
