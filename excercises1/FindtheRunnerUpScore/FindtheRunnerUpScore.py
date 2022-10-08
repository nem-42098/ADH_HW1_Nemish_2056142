if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l1=list(arr)
    l1.sort(reverse=True) ## Arrange in descending order
    y=[i for i in l1 if i!=l1[0]] ##Remove the top winner
    print(y[0])
