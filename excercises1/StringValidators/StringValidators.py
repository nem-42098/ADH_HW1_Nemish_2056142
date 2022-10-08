if __name__ == '__main__':
    s = input()
    s_split=[i for i in s]
    for j,i in enumerate(s_split):
        if i.isalnum():
            print('True')
            break
        elif j==len(s_split)-1:
            print('False')   
    # if i.isalnum():
    #         print('True')
    #         break
    # else 
    #         print('False')
    for j,i in enumerate(s_split):
        if i.isalpha():
            print('True')
            break
        elif j==len(s_split)-1:
            print('False')
    for j,i in enumerate(s_split):
        if i.isdigit():
            print('True')
            break
        elif j==len(s_split)-1:
            print('False')
    for j,i in enumerate(s_split):
        if i.islower():
            print('True')
            break
        elif j==len(s_split)-1:
            print('False')
    for j,i in enumerate(s_split):
        if i.isupper():
            print('True')
            break
        elif j==len(s_split)-1:
            print('False')
