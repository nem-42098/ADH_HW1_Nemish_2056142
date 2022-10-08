if __name__ == '__main__':
    N = int(input())
    l3=[] ## input
    l2=[] ## commmand
    l1=[]
    for _ in range(N):
        b,*a=input().split()
        l2.append(b)
        l3.append(a)

    for j,i in enumerate(l2):
        if i=='insert':
            l1.insert(int(l3[j][0]),int(l3[j][1]))
        elif i=='print':
            print(l1)
        elif i=='remove':
            l1.remove(int(l3[j][0]))
        elif i=='append':
            l1.append(int(l3[j][0]))
        elif i=='sort':
            l1.sort()
        elif i=='pop':
            l1.pop()
        else:
            l1.reverse()
                
