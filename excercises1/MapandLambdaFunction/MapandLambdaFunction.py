cube = lambda x:x*x*x # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    
    if n>1:
        l_fb=[0,1]
        for i in range(n-2):
            
                l_fb.append(l_fb[i]+l_fb[i+1])
    elif n==0:
            l_fb=[]
    elif n==1:
            l_fb=[0]
        
          
    return l_fb
