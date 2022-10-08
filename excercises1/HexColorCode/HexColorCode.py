# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
j=0
k=0
s=''
for i in range(n):
    in1=input()
    if ('{' in in1):
        j=1
    
    elif ('}' in in1):
    
        j=0
    elif j==1:
        s=s+in1
#print(s)       
regex=r'\#[a-fA-F0-9]{3,6}'
y=re.findall(regex,s)
for k in y:
    print(k)
