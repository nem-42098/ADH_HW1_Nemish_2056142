# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M=input().split()
N=int(N)
M=int(M)

thicknes=M
a='|'
b='.'
for i in range(N):
    x=''
    if i <N//2:
        for j in range(2*i+1):
            x=x+b+a+b
    elif i==N//2:
        x='WELCOME'
    else:
        for j in range(2*(N-i)-1):
            x=x+b+a+b
    print(x.center(thicknes,'-'))
