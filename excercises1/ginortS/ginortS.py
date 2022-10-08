# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
char=[]
number=[]
for i in s:
   if i.isalpha():
     char.append(i)
   if i.isnumeric():
     number.append(int(i))
char.sort()
char_lower=[]
char_upper=[]
for i in char:
    if i.isupper():
    
        char_upper.append(ord(i))
    else:
        char_lower.append(ord(i))
char_upper.sort()
char_lower.sort() 
number.sort()
number_odd=[]
number_even=[]
for i in number:
    if int(i%2)==0:
    
        number_even.append(i)
    else:
        number_odd.append(i)
s=''
for j in char_lower:
    s=s+chr(j)
for i in char_upper :
    s=s+chr(i)

for k in number_odd:
    s=s+str(k)
for l in number_even:
    s=s+str(l)
print(s)
