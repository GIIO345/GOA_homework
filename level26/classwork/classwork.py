#kata 1
def cookie(x):
    if type(x)==str:
        return "Who ate the last cookie? It was Zach!"
    if  type(x)==int or type(x)==float:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"

#kata 2
def multiply(n):
    return n*5**len(str(abs(n)))