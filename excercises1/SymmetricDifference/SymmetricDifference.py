# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
set_a=set(list(map(int,input().split())))
N=int(input())
set_b=set(list(map(int,input().split())))
l_un=set_a.intersection(set_b)
sym_a=set_a.difference(set(l_un))

sym_b=set_b.difference(set(l_un))
sym_c=list(sym_a.union(sym_b))
sym_c.sort()
for i in sym_c:
    print(i)

