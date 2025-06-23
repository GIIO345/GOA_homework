#1) მომხმარებელს შემოაყვანინეთ რიცხვი. თუ ის ლუწია გამოიტანეთ სიტყვა "ლუწი", ხოლო თუ კენტია გამოიტანეთ "კენტი"
Num1=int(input("eneter num"))
if Num1%2==0:
    print("ricxvi luwia")
if Num1%2==1:
  print("kentia")
  #2) შეამოწმეთ რიცხვი ნეგატიურია პოზიტიურია თუ 0-ია. ამის მიხედვით გაუტოლეთ ცვლად res 0, -1 ან 1
num1=int(input("enter number"))
if num1==0:
    print("it is equal to zero")
elif num1>0:
    print("number is positive")
elif num1<0:
    print("number is negative")
   #) მომხმარებლს შემოატანინეთ 2 რიცხვი და გამოიტანეთ უდიდესი ტერმინალში. 
number=int(input("enter a number: "))
number2=int(input("enter a number2: "))
if number>number2:
    print(number)
elif number2>number:
    print(number2)
    
    #4) შემოაყვანინეთ მომხმარებელს რიცხვი. თუ ის 5-ზე იყოფა გამოიტანეთ შემოყვანილი რიცხვი, ხოლო თუ არ იყოფა მაშინ გამოიტანეთ რიცხვი 0.
ricxvi=int(input("shemoiyvanet ricxvi"))

if ricxvi%5==0:
    print(ricxvi)
elif ricxvi/5>=1:
    print("0")
#5) შეამოწმეთ თუ მომხმარებლის შემოყვანილი რიცხვი ახალი საუკუნის რიცხვია. თუ ახალი საუკუნის არის (მაგ 2000) გამოიტანეთ "ახალი საუკუნე".
nummm=int(input(("enter numm")))
if nummm>2000:
    print("ახალი საუკუნე")