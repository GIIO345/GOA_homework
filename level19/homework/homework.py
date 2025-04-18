
#შექმენით ფუნქცია, რომელიც აერთებს ორ ლისტს (ორივეში მხოლოდ integer-ებია) და ასევე ალაგებს მათ ზრდადობის მიხედვით
lith=[23,43,2,31,387,5,25,46,3,654,]
litl=[97,96,7,587,58,79,67,6]
def ascending_order(lith,litl):
    res=[]
    for i in lith:
        res.append(i)
    for i in litl:
        res.append(i)
    res.sort()
    return res
print(ascending_order(lith,litl))


#შექმენით ფუნქცია რომელიც არგუმენტებად იღებს ორ ლისტს და გამოაქვს ის, რომლის ელემენტებთა ჯამი (iteger-თა) უფრო მეტია.
listk=[23,34,45,7,67,86,]
listj=[23,54,6,54,765,]
def more(listk,listj):
    sum1=0
    sum2=0
    for i in listk:
        sum1+=i
    for i in listj:
        sum2+=i
    if sum1>sum2:
        return "listk"
    return "listj"
print(more(listk,listj))
            
        

#შექმენით ფუნქცია რომელიც იღებ არგუმენტებად ორ ლისტს და აბრუნებს დადებითი რიცხვების რაოდენობასა და უარყოფითების ჯამს (ცალ-ცალკე).

O=[2,3,343,-43,-343,-12,-23]
K=[-34,35,-675,43,-343,-3,434,43]
def exemine(O,K):
    se=0
    su=0
    sa=0
    sk=0
    for i in O:
        if i<0:
            se+=i
        else:
            su+=1
    for i in K:
        if i<0:
            sa+=i
        else:
            sk+=1
    return f"-O:{se}\n+O:{su}\n-K{sa}\n+K{sk}"
print(exemine(O,K))
    







#შექმენით ფუნქცია რომელიც არგუმენტად იღებს ლისტს და შლის ყველა ელემენტს რომელიც უნაშთოდ იყოფა 3-ზე
list_a = [3, 5, 9, 12, 16, 18, 20]
def  noreminder(list_a):
    res=[]
    for i in list_a:
        if i%3!=0:
            res.append(i)
    return res
print(noreminder(list_a))




#შექმენით ფუნქცია რომელსაც გამოაქვს არგუმენტად გადაცემული ლისტის ფორმა, სადაც ყველა ელემენტი გარომაგებულია 2-ზე, 
# მაგალითად input: [2,3,4,5], output: [4,6,8,10] 
list_k=[353,654,674,576,]
def twotimes(list_k):
    ref=[]
    for i in list_k:
        ref.append(i*2)
    return ref
print(twotimes(list_k))


