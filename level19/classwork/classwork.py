

#1) codewars make a toast
def six_toast(num):
    if num==6:
        return
    if num!=6:
        res=num-6
        return abs(res)
#2) შექმენით ორი ლისთი და ლუპის მეშევოებით შექმენით ახალი ლისთი რომელიც იქნება ამ ორის გაერთანება
listf=[23,2,32,4,32,43,23,4]
listd=[6,7,86,8,76,87,5,6,4]
res=[]
for i in listf:
    res.append(i)
for i in listf:
    res.append(i)
print(res)

#3) შექმენით ფუნქცია რომელიც იღებს მასივს და აბრუნებს ახალ მასივს კენტი ელემენტების გარეშე
listk=[23,542,342,2312,13542,]
res=[]
def even(listk):
    
    for i in listk:
        if i%2==0:
            res.append(i)
    return res
print(even(res))
#4) შექმენით ფუნქცია რომელიც იღებს მასივს ინტეჯერების და დააბრუნებს სტრინგ ამ ინტეჯერების გაერთიანების. მაგ ( [1,2,4,18] --->  "12418"  ) (edited)
listg=[23,2,43,321,4,]

def string(listg):
    string=''
    for i in listg:
        string+=str(i)
    return string
print(string(listg))

#5) code wars 
a="code"
b="wa.rs"
name=a+b
    

