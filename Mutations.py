def mutate_string(string, position, character):
    l1=list(string)
    l1[position]=character
    l2="".join(l1)
    return l2
