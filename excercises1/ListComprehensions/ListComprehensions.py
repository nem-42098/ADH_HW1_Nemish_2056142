if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list_of_c=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                list_of_c.append([i,j,k])
    final_list=[l for l in list_of_c if l[0]+l[1]+l[2] !=n ]
    print(final_list)
