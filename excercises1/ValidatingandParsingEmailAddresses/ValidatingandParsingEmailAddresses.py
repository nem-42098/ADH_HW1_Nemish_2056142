# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
import re
x=[]
y=[]
for _ in range(n):
  x,y=input().split()  
  regex=r'\<[a-zA-Z][a-zA-Z0-9\-\.\_]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}\>'
  if bool(re.match(regex,y)):
    print(x,y)
