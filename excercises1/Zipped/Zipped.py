# Enter your code here. Read input from STDIN. Print output to STDOUT
N_stud,N_sub=map(int,input().split())
l_sub=[]
for i in range(N_sub):
    l_sub.append(list(map(float,input().split())))
z=zip(*l_sub)
for i in z:
    print(sum(i)/N_sub)

