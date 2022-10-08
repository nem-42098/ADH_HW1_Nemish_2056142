# Enter your code here. Read input from STDIN. Print output to STDOUT
N_test=int(input())
for i in range(N_test):
    m1=int(input())
    set_a=set(list(map(int,input().split())))
    m2=int(input())
    set_b=set(list(map(int,input().split())))
    if(len(set_a & set_b)==m1):
        print('True')
    else:
        print('False')
    
