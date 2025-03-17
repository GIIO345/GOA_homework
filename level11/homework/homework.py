
def calculator(x, y, op):
    if type(x)==int and type(y)==int:
        if op=="+":
            return x+y
        if op=="-":
            return x-y
        if op=="*":
            return x*y
        if op=="/":
            return x/y
        else:
            return "unknown value"
    else:
        return "unknown value"
        
    

def string_clean(s):
    word=""
    for i in s:
        if i not in ("1234567890"):
            word+=i
    return word

def count_char_occurrences(strng, char):
    count=0
    for i in strng:
        if i==char:
            count+=1
    return (count)
