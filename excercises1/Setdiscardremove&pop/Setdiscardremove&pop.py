n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    x=list(input().split())
    if x[0]=='pop':
        s.pop()
    elif x[0]=='remove':
        s.remove(int(x[1]))
    else:
        s.discard(int(x[1]))
sum=0
for i in s:
    sum=sum+i
print(sum)
