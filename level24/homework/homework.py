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
def abbrev_name(name):
    name1,name2=name.split()
    return f"{name1[0].upper()}.{name2[0].upper()}"


#kata4
def rps(p1, p2):
    
    if (p1=="rock" and p2=="rock") or (p1=="paper" and p2=="paper") or (p1=="scissors" and p2=="scissors"):
        return "Draw!"
    elif (p1=="scissors" and p2=="paper") or (p1=="rock" and p2=="scissors") or (p1=="paper" and p2=="rock") :
        return "Player 1 won!"
    else:
        return "Player 2 won!"

#kata5
def feast(beast, dish):
    return beast[0]==dish[0] and beast[-1]==dish[-1]