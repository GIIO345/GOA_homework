#kata 1
def remove_char(s):
    return s[1:-1]


#kata2
def positive_sum(arr):
    return sum(i for i in arr if i>0)

#kata 3
def sum_array(a):
    if a=="":
        return "0"
    else:
        return sum(i for i in a)
    

#kata 4
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old-son_years_old*2)

#kata 5
def digitize(n):
    rel = []
    n = str(n)
    res = n[::-1]  
    for i in res:  
        rel.append(int(i))
    return rel