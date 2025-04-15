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
listo=[23,-4254,-35,-3,-65,7,]
listp=[3,34,-2,4,-35,5,-65,]
def func(listo,listp):
    sum1=0
    sum2=0
    count1=0
    count2=0
    for i in listo:
        if i<0:
            sum1+=i
    for i in listp:
        if i<0:
            sum2+=i
    for i in listo:
        if i>0:
            count1+=1
    for i in listp:
        if i>0:
            count2+=1
    return f"-listo{sum1}\n-listp{sum2}\n+listo{count1}\n+listp{count2}"
print(func(listo,listp))

listn = [23, -4254, -35, -3, -65, 7]
listb = [3, 34, -2, 4, -35, 5, -65]

def funct(listo, listp):
    sum1 = sum(i for i in listn if i < 0)
    sum2 = sum(i for i in listb if i < 0)
    count1 = sum(1 for i in listn if i > 0)
    count2 = sum(1 for i in listb if i > 0)
    
    return f"-listn {sum1}\n-listb {sum2}\n+listn {count1}\n+listb {count2}"

print(funct(listn, listb))




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