
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