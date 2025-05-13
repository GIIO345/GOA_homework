""""
შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან არგუმენტს და მისი type-ის სესაბამისად გამოიტანეთ სიტყვები:
Str - "Literature"
Int/Float - "Math"
Bool - "Science"


def typer(a):
    if type(a)==str:
        return "Literature"
    elif type(a)==int or type(a)==float:
        return "Math"
    return "Science"


    
შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს ლისტს და გამოიტანეთ ის data type რომელიც ყველაზე ხშირად გვხვდება ამ ლისტსში.
"""""
def listf(a):
    return max(type()) in a
print(listf(["a", "a", "a", 1 > 0, 0 > 1, 1 > 8, 1, 2, 0.3, 2.3, 33, 3, 3]))

