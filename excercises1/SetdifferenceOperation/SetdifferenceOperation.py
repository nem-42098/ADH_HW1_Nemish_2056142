# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set_n=set(list(map(int,input().split())))
b=int(input())
set_b=set(list(map(int,input().split())))
union=set_n-set_b
print(len(union))
