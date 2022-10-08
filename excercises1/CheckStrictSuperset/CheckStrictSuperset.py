# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a=set(list(map(int,input().split())))
N_os=int(input())
count=0
for i in range(N_os):
    set_os=set(list(map(int,input().split())))
    inter=set_os & set_a
    if (len(inter)==len(set_os)) and (len(set_a & inter)>0) :
        count=count+1
if count==N_os:
    print('True')
else:
    print('False')
