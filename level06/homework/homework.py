#1) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ for ციკლის გამოყენებით, გამოთვალეთ და გამოიტანეთ მხოლოდ კენტი რიცხვების ჯამი
number=int(input("enter the number"))
count=0
for i in range (2,number):
    if i%2==1:
        count+=i
        print(count)

#2)მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ for ციკლის გამოყენებით გამოიტანეთ მხოლოდ ის რიცხვები, რომლებზეც უნაშთოდ იყოფა შემოტანილი რიცხვი

num1=int(input("enter the number"))
count=0
for Q in range(1,num1):
    if num1%Q==0:
        print(Q)

#3)ამ კოდს დაამატეთ ლოგიკა, რომ 3 არასწორი პაროლის შეყვანის შემდეგ კოდი გაჩერდეს
num = int(input("please input a number: ")) 
count=0
while num==1:
       num=int(input("try another number: "))
for i in range(2,num):
    if num % i == 0 and count == 0:
        print('Your number is not a prime')
        count+=0
if count == 0:
    print('your number is a prime')


number=int(input("enter prime number"))
count=0
for i in range(2,number):
    if number%i==1:
        print("you guessed number right")
    elif number%i==0:
        while number%i==0:
            count=count+1
            number=int(input("enter prime number"))
            if count==3:
                break
          

        






#4)ეს შედარებით რთულია და თუ ვერ გააკეთეთ არაუშავრა
#მომხმარებელს შემოატანინეთ რაიმე stringი და for ციკლის გამოყენებით დააბრუნეთ ეს სტრინგი შემოტრიალებული

word=input("enter word")
res=""

for _ in word:
    res=_+res
    print(res)





