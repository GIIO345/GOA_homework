"""""
#შექმენით ფუნქცია სადაც მომხმარებელი გადასცემს ორ არგუმენტს, ორივე არის რიცხვი მაგრამ არ იცით თუ როგორი სახითაა იგი ჩაწერილი (string თუ integer), თქვენი დავალებაა შეკრიბოთ ეს ორი რიცხვი, მაგრამ გაითვალისწინოთ ისიც, რომ მომხმარებელმა შეიძლება შმეოიტანოს boolean ან float (String-ში ყოველთვის იქნება რიცხვები).
def add_var(a,b):
    if type(a)==bool:
        a=0
    elif type(a) in (str,float):
        a=int(float(a))
    if type(b)==bool:
        b=0
    elif type(b) in (str,float):
        b=int(float(b))
    res=a+b
    return res

#შექმენით ფუნქცია სადაც მომხარებელი გასაცემს ასევე ორ არგუმენტს, თქვენი დავალებაა რომ უფრო დიდი რიცხვი გაყოთ უფრო პატარაზე (ასევე არ იცით რა მონაცმეთა ტიპია), თუ გამყოფი აღმოჩნდება 0 გამოიტანეთ ZeroDivissionError
def div(k,l):
    if type(k)==bool:
        k=0
    elif type(k) in (str,float):
        k=int(float(k))
    if type(l)==bool:
        l=0
    elif type(l) in (str,float):
        l=int(float(l))
    if k>l:
        if l==0:
            return "ZeroDivissionError"  
        else:
            return k/l 
    if l>k:
        if k==0:
            return "ZeroDivissionError"  
        else:
            return l/k
print(div(5,0))

#შექმენით ფუნქცია რომელიც დაუმატებს ერთმანეთს string-ებს რომელიც გადმოეცემა არგუმენტად, გაითვალისწინეთ რომ თუ რომელიმე არგუმენტი იქნება ineger ის უნდა მოათავსოთ შედგენილი წინადადების ბოლოშო.
def HD(p,d):
    if type(p)==int:
        return f"{d}{p}"
    elif type(d)==int:
        return f"{p}{d}"
print(HD(2,"dsd"))
"""

#შეეცადეთ შექმნათ ფუნქცია, სადაც მომხმარებელი შეიყვანს რამე ორ არგუმენტს, მაგალითად "Goa" და Str, თქვენ უნდა შეამოწმოთ ემთხვევა თუ არა პირველი არგუმენტი მეორეს, ამ შემთხვევასი იქნება True რადგან "Goa" მართლაც არის String.
def stro(s,j):
    return type(s)==j 
print(stro("ds",str))
        
    