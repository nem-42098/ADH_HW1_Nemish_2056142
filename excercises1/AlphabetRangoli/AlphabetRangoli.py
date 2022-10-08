def print_rangoli(size):
    # your code goes here
    l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    thickness=2*size+2*(size-1)-1
    for i in range(2*size-1):
        
        if i < size-1:
            s=[]
            for j in range(i+1): ### pick up the unique characters
                s.append(chr(97+size-1-j))
            var=len(s)
            for k in range(var-1): ### create the list of all the required characters
                 s.append(s[var-k-2])
           
    
            a=''
            for l in s:  ### create the '-'+characters
               a=a+l+'-'
            print(a.center(thickness,'-')) 
        if i==size-1:  ### middle line
            s=[]
            for j in range(i+1):
                s.append(chr(97+size-1-j))
            var=len(s)
            for k in range(var-1):
                s.append(s[var-k-2])
            a=''
            for l in s:
                a=a+l+'-'
          
            
            print(a.strip('-'))
        if i>size-1:
            s=[]
            for j in range(2*size-(i+1)): ### pick up the unique characters
                s.append(chr(97+size-1-j))
            var=len(s)
            for k in range(var-1): ### create the list of all the required characters
                s.append(s[var-k-2])
            a=''
            for l in s:  ### create the '-'+characters
               a=a+l+'-'
            print(a.center(thickness,'-')) 
