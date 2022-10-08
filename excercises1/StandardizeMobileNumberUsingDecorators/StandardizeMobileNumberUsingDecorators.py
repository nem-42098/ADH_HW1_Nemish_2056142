def wrapper(f):
    def fun(l):
        # complete the function
    
        list1=[]
        #print(l)
        for i in l:
            if len(i)>10:
        
                list1.append('+91'+' '+i[-10:-5]+' '+i[-5:])
            else:
                list1.append('+91'+' '+i[0:5]+' '+i[5:10])
        x=sorted(list1)
        print(*x,sep='\n' )
    
    return fun

