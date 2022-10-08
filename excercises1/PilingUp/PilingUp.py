# Enter your code here. Read input from STDIN. Print output to STDOUT
N_test=int(input())
for i in range(N_test):
    test_n_blocks=int(input())
    x=list(map(int,input().split()))
    if (max(x)==x[0]) or (max(x)==x[-1]):
        print('Yes')
    else:
        print('No')
