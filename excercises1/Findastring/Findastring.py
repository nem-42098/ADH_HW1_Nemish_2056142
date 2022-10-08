def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        sub_length=len(sub_string)
        if string[i:sub_length+i]==sub_string:
            count=count+1
    return count

