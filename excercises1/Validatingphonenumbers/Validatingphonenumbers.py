# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
import re
for _ in range(n):
    in1=input()
    if len(in1)==10:
        regex=r'[7|8|9][0-9]{9}'
        if bool(re.match(regex,in1)):
            print('YES')
        else:
            print('NO')
    else:
            print('NO')
