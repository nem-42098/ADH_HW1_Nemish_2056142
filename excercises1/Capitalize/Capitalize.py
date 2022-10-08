

# Complete the solve function below.
def solve(s):
    ind=s.split()
    list1=[]
    counter=[]
    k=0
    for o in s:
        
        if o.isspace():
            k=k+1
        else:
            if k>=1:
                counter.append(k)
            k=0
    #print(counter)
            
    for j,i in enumerate(ind):
        #print(j,i)
        if i[0].isalpha():
            s=''
            for l,k in enumerate(i):
                #print(l,k)
                if l==0:
                    s=s+k.upper()
                else:
                    s=s+k
            list1.append(s)
        else:
            list1.append(i)
    fin_str=''
    for j,i in enumerate(list1):
        if j<len(list1)-1:
            fin_str=fin_str+i+' '*counter[j]
        else:
            fin_str=fin_str+i
    return fin_str
            
