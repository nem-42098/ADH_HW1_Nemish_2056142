# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
def correct(match):
    if match.group(0)=='&&':
        return 'and'
    else:
        return 'or'
for i in range(N):
    in1=input()
    print(re.sub(r'(?<=\s)(&&)(?=\s)|(?<=\s)\|\|(?=\s)',correct,in1))
    
