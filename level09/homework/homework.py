"""""
1)
a="gio"
b=5
def multiply(a,b):
    return (a*b)
print(multiply(a,b))

2)
def repeat_str(repeat,string):
    return string*repeat
print(repeat_str(3,"a"))

3)
def get_grade(s1, s2, s3):
    average=(s1+s2+s3)/3
    if average<=100 and average>=90:
        return "A"
    elif average<=90 and average>=80:
        return "B"
    elif average<80 and average>=70:
        return "C"
    elif average<70 and average>=60:
        return "D"
    elif average < 60 and average>=0:
        return "F"
4)
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8 
    else:
        return number * 9
5)
def rps(p1, p2):
    if (p1=="rock" and p2=="rock") or (p1=="paper" and p2=="paper") or (p1=="scissors" and p2=="scissors"):
        return "Draw!"
    elif (p1=="scissors" and p2=="paper") or (p1=="rock" and p2=="scissors") or (p1=="paper" and p2=="rock") :
        return "Player 1 won!"
    else:
        return "Player 2 won!"

#შექმენით ფუნქცია რომელსაც გადაეცემა ორი პარამეტრი name, lastname. თქვენი დავალებაა გამოიტანოთ სახელის პირველი ასო, წერტილი და გვარი, მაგალითად:
name=input("enter your name: ")
surname=input("enter your surname: ")
def initials(name,surname):
    return f"{name[0]}.{surname}"
print(initials(name,surname))
"""
