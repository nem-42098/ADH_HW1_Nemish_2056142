if __name__ == '__main__':
    n = int(input())
    if n>=1 and n<=150:
        for i in range(1,n+1):
            print(i,end='')
    else:
        print( 'Enter a number between 1 and 150')
