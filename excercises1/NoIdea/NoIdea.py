# Enter your code here. Read input from STDIN. Print output to STDOUT
m,n= [int(x) for x in input().split()]
array=[int(x) for x in input().split()]
set_a=set()
for x in input().split():
    set_a.add(int(x))
set_b=set()
for x in input().split():
    set_b.add(int(x))
happiness=0  
for i in array:
   if i in set_a:
        happiness=happiness+1
   if i in set_b:
        happiness=happiness-1
print(happiness)
    
