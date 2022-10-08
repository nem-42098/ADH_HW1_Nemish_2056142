def swap_case(s):
    x=''
    for i in range(len(s)):
        
        if s[i].islower():
           x=x+s[i].upper()
        else:
           x=x+s[i].lower()
    return x.strip()

