
#1 
def check_alive(health):
    return health>0
#2
def repeat_str(repeat, string):
    p=""
    p=string*repeat
    return p
#3
def cookie(x):
    if type(x)==str:
        return "Who ate the last cookie? It was Zach!"
    if  type(x)==int or type(x)==float:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"

#4
def century(year):
    p=(year+99)//100
    return p
#5
def find_average(nums):
    all=sum(nums)
    res=all/len(nums)
    return res        
