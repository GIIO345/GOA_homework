#kata 1
def digitize(n):
    j=[]
    for i in str(n):
        j.append(int(i))
    res=j[::-1]
    return res
    