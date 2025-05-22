
# მომხმარებელი შეიყვანს დღეს, თვეს და წელიწადს ცალ-ცალკე. დაბეჭდე თარიღი შემდეგი ფორმატით: "დღე/თვე/წელი",

# მაგალითად:,
# შეიყვანე დღე: 14,
# შეიყვანე თვე: 5,
# შეიყვანე წელი: 2025,
# თარიღი: 14/5/2025

date=input("შეიყვანე დღე: ")
month=input("შეიყვანე თვე: ")
year=input("შეიყვანე წელი: ")
def info(date,month,year):
    return f"თარიღი: {date}/{month}/{year}"
print(info(date,month,year))


# პაროლი

# მომხმარებელი შეიყვანს პაროლს. თუ პაროლი 8-ზე ნაკლები სიმბოლოა — დაბეჭდე "პაროლი ძალიან მოკლეა", თუ 8 ან მეტი — "პაროლი მიღებულია".

password=int(input("make a password: "))
def passw(password):
    if password<8:
        return "ნალკლებია რვაზე"
    return "პაროლი მიღებულია"
print(passw(password))

# მაქსიმალური რიცხვის პოვნა,
# ,
# მომხმარებელი შეიყვანს სამ მთელ რიცხვს. დაბეჭდე რომელი მათგანი არის ყველაზე დიდი.

num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))
def Maxx(num1,num2,num3):
    res=[]
    res+=num1,num2,num3
    return max(res)
print(Maxx(num1,num2,num3))


# რიცხვების ჯამი სიაში,
# ,
# მომხმარებელს შემოატანინე 5 რიცხვი ერთის შემდეგ მეორე, შეინახე ისინი სიაში (list-ში) და ბოლოს დაბეჭდე მათი ჯამი.

num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))
num4=int(input("enter num4: "))
num5=int(input("enter num5: "))
def summ(num1,num2,num3,num4,num5):
    res=[]
    res+=num1,num2,num3,num4,num5
    return sum(res)
print(summ(num1,num2,num3,num4,num5))



#განახლებული კოდის ვერსია
# მომხმარებელი შეიყვანს დღეს, თვეს და წელიწადს ცალ-ცალკე. დაბეჭდე თარიღი შემდეგი ფორმატით: "დღე/თვე/წელი",

# მაგალითად:,
# შეიყვანე დღე: 14,
# შეიყვანე თვე: 5,
# შეიყვანე წელი: 2025,
# თარიღი: 14/5/2025


def time(day,month,year):
    months=["January, February, March, April, May, June, July, August, September, October, November, December"]
    for i in months:
        if month.lower()==i:
            month=i
        elif month is int and 1>=abs(month)<=12:
            pass
    if day is str and 1>=abs(int(day))<=31:
        day=abs(int(day))
    if year is str:
        year=abs(int(year))
    return f"{day}/{month}/{year}"
print(time("21","13","2000"))




    
# მომხმარებელს შემოატანინე 5 რიცხვი ერთის შემდეგ მეორე, შეინახე ისინი სიაში (list-ში) და ბოლოს დაბეჭდე მათი ჯამი.

def summe(n1, n2, n3, n4, n5):
    return sum([n1, n2, n3, n4, n5])
print(summe(23,3,2,5,6))

# მომხმარებელი შეიყვანს პაროლს. თუ პაროლი 8-ზე ნაკლები სიმბოლოა — დაბეჭდე "პაროლი ძალიან მოკლეა", თუ 8 ან მეტი — "პაროლი მიღებულია".
a=input("enter your password: ")
def ps(a):
    while len(a)<8:
        print("თვენი პაროლი ძალიან მოკლეა")
        a=input("enter your password: ")
    return "პაროლი მიღებულიაა"
print(ps(a))
    