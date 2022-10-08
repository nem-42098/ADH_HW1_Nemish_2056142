

def person_lister(f):
    def inner(people):
        # complete the function
        
        list1=[]
        for p in people:
            p[2] = int(p[2])
        people.sort(key=operator.itemgetter(2))
        for i in people:
            list1.append(f(i))
        return list1
    return inner

