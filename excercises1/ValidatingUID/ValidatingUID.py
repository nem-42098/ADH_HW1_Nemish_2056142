# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
in1=int(input())
for _ in range(in1):
    in2=input()
    regex=r'[A-Z]{1,7}|[0-9]{1,8}|[a-z]{1,5}'
    m=re.findall(regex,in2)
    j=0
    s=''
    upper=0
    digit=0
    z=5
    for i in m:
        for k in i:
            if k not in s:
                if k.isupper():
                    upper=upper+1
                if k.isdigit():
                    digit=digit+1
                s=s+k
                j=j+len(k)
            else:
                z=0
                print('Invalid')
                break
        if z==0:
            break
            
    if j==len(in2) and (upper>=2) and (digit>=3):
                print('Valid')
            
    #print(upper,digit)        
    if  (upper<2) or (digit<3):
        if z!=0:   
            print('Invalid')
    
