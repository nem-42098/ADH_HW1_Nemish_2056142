# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

in1=input()
m=re.findall(r'(?<=[^aAeEiIoOuU])[aAeEiIoOuU]{2,100}(?=[^aAeEiIoOuU])',in1)
if m!=[]:
    for i in m:
        print(i)
else:
        print(-1)
