#kata 1
def digitize(n):
    j=[]
    for i in str(n):
        j.append(int(i))
    res=j[::-1]
    return res

#kata 2
def to_alternating_case(string):
    word=""
    for i in string:
        if i.islower():
            word+=i.upper()
        elif i.isupper():
            word+=i.lower()
        else:
            word+=i
    return word

#kata3
