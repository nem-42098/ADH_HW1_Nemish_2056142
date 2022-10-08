# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
in1=input()
in2=input()
i=0
j=0

while j<len(in1)-1:
    #print(in1[j:])
    
    m=re.search(r''+in2+'{1}',in1[j:])
    if (m!=None) and (j>=0):
        if (len(in2)>1) :

                print((m.start()+j,m.end()-1+j))
                i=m.end()-1
                j=j+i
                #print(j)
                
        
        elif len(in2)==1:
            
                print((m.start()+j,m.end()-1+j))
                i=m.end()
                j=j+i
                #print(j)
                
    elif m==None:
        if j==0:
            print((-1,-1))
            j=len(in1)
        else:
            j=len(in1)
            
