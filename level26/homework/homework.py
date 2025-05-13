
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

def litf(a):
    strf=0
    intf=0
    floatf=0
    boolf=0
    for i in a:
        if type(i)==str:
            strf+=1
        elif type(i)==int:
            intf+=1
        elif type(i)==float:
            floatf+=1
        else:
            boolf+=1
    return max("string"+str(strf),"int"+str(intf),"float"+str(floatf),"bool"+str(boolf))
print(litf([True, False, "hello", "world","i", "python", 42, 100, -7, 3.14, 2.718, 0.001]))



#შექმენით ფუნქცია, რომელსაც გადაეცემა list, თუ ამ ლისტში არის ყველა integer და ერთი string ან სხვა ნებისმიერი data type, თქვენ უნდა დააბრუნოით იგივე list #განსხვავებული data type-ის გარეშე.
def func(a):
    lf = []
    for i in a:
        if type(i) in (bool, str, float):
            lf.append(int(i))
    return lf
print(func([True, False, "1", "1","1", "1", 42, 100, -7, 3.14, 2.718, 0.001]))



#შექმენით ფუნქცია სადაც მომხარებელი შეიყვანს რაიმე მათემატიკურ ოპერაციას და თქვენ უნდა დააბრუნოთ საბოლოო პასუხის type.
def meth(a):
    return type(a)
  