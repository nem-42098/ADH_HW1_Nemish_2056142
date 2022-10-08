



def get_attr_number(node):
    # your code goes here
    sum=0
    sum=sum+len(node.attrib)
    for i in node:
        sum=sum+get_attr_number(i)

     
    return sum

