def make_negative( number ):
    if number<=0:
        return number
    return int(f"-{number}")

def solution(string):
    res=""
    for i in string:
        res=i+res
    return res

def number_to_string(num):
    return str(num)