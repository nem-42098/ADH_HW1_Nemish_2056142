def mutate_string(string, position, character):
    l1=list(string)
    l1[position]=character
    string=''.join(l1)
    return string

