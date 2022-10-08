# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d=deque()
M=int(input())
for i in range(M):
    cmd=input().split()
    if cmd[0]=='append':
        d.append(cmd[1])
    elif cmd[0]=='appendleft':
        d.appendleft(cmd[1])
    elif cmd[0]=='pop':
        d.pop()
    else:
        d.popleft()
print(*d)
        
