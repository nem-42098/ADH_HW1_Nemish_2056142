if __name__ == '__main__':
    n = int(input())
    if n>=1 and n<=20: # Checking the constraint
        for i in range(n):
            print(i*i)
    else:    
         print(' Choose a number between 1 and 20')   
