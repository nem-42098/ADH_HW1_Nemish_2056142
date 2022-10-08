def merge_the_tools(string, k):
    # your code goes here
    
    len_sub=int(len(string)/k)
    
    
    l_sub=[]
    for i in range(len_sub):
        l_sub.append(string[i*k:i*k+k])
    ul_sub=[]
    for j in l_sub:
        
        x=''
        for k in j:
            sub_set=set(x)
            if k in sub_set:
               continue
            else:
    
               x=x+k
        ul_sub.append(x)
    for k in ul_sub:
        print(k)
                
