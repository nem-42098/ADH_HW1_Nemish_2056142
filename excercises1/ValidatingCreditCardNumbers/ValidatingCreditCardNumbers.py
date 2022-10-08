# Enter your code here. Read input from STDIN. Print output to STDOUT
in1=int(input())
import re
for _ in range(in1):
    in2=input()
    regex='^([4|5|6][0-9]{3}-?)([0-9]{4}-?)([0-9]{4}-?)([0-9]{4})$'
   
    k=0
    s=''
    in3=in2
    in3=in3.replace('-','')
    for i,j in enumerate(in3):
        if i>0:
            #print(s,s[-1],j,k)
            if s[-1]==j:
                
            
                k=k+1
                
                if k==3:
                    print("Invalid")
                    break
            else:
                k=0   
            s=s+j
        elif k==3 :
            break
        else:
            s=s+j
            
    if re.match(regex,in2)==None and k!=3:
                  print('Invalid')
                
    elif (re.match(regex,in2)!=None) and k!=3:
              print('Valid')
