# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
N=list(map(int,input().split()))
set_N=set(N)
var=sum(set_N)*M-sum(N)
print(var//(M-1))
