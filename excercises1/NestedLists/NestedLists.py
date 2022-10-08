if __name__ == '__main__':
    list1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
    def sort_func(l):
        return l[1]
    list1.sort(reverse=True,key=sort_func)
    
    k=len(list1)-1
    min_1=list1[k][1]
    min_2=-100000
    while min_2 <= min_1:
            if list1[k-1][1]==list1[k][1] and k>0:
                k=k-1
          
            else:
                min_2=list1[k-1][1]
                

   # min_2=list1[k-1][1]
    second_runner=[y for y in list1 if y[1]==min_2]

    def sort_func2(l):
        return l[0][0]
    second_runner.sort(key=sort_func2)
    for i in second_runner:
        print(i[0])
