

def wrap(string, max_width):
    l=textwrap.wrap(string,width=max_width)
    s=''
    for i in l:
        s=s+i+'\n'
        
    return s

