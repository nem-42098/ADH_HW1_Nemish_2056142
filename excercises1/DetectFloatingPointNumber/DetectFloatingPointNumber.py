# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
for i in range(N):
    test_case=input()
    try:
        f_test=float(test_case)
        a=False
        b=False
        if bool(re.search(r'\.', test_case)) and not(test_case[-1]=='.'):
                a=bool(re.search(r"\+",test_case))
                b=bool(re.search(r'\-',test_case))
                if (a and not(b)) or (not(a) and b):
                    print('True')
                elif not(a) and not(b):
                    print("True")
        else:
            print('False')            
        
    except:
         print('False')
