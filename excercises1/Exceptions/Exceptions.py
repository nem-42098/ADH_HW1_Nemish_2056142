# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases=int(input())
for i in range(test_cases):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print('Error Code:'+' integer division or modulo by zero')
    except ValueError as e:
        print('Error Code:',e)
