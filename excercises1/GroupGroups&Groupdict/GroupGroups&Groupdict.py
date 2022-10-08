# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
in1=input()
m=re.search(r'([a-z0-9])\1',in1)
if m!=None:
    print(m.group(0)[0])
else:
    print(-1)
