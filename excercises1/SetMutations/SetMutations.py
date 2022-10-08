# Enter your code here. Read input from STDIN. Print output to STDOUT
N_a=int(input())
set_a=set(list(map(int,input().split())))
N_os=int(input())
for i in range(N_os):
    cmd,len_os=input().split()
    set_os=set(list(map(int,input().split())))
    if cmd=='intersection_update':
        set_a.intersection_update(set_os)
    elif cmd=='symmetric_difference_update':
        set_a.symmetric_difference_update(set_os)
    elif cmd=='update':
        set_a.update(set_os)
    elif cmd=='difference_update':
        set_a.difference_update(set_os)
    
sum=0
for i in set_a:
    sum=sum+i
print(sum)
