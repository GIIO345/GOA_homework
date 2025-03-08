#For loop-ის დახმარებით შექმენით პროგრამა, სადაც მომხმარებელი შემოიტანს რიცხვს (50-ის ჩათვლით, თუ არა დაუპრინტეთ, რომ თავიდან შეიყვანოს), და თქვენ გამოიტანეთ ამ რიცხვის ჯერადები 100-ის ჩათვლით.
number=int(input("enter a number"))
while number <0 or number>50:
    print("try again")
    number=int(input("enter a number"))
    for i in range(number,100):
      if i%number==0:
         print(i)
## 5. შექმენით პატარა თამაში, სადაც თქვენ შექმნით რაიმე რიცხვების თანმიმდევრობას (ოთხნიშნა integer-რიცხვი), და მომხმარებელმა კი უნდა გამოიცნოს ეს თანმიმდევრობა (გამოიყენეთ While loop)
sequence=(3456)
list=int(input("enter the sequence"))
while sequence!=list:
   list=int(input("enter the sequence"))
if sequence==list:
   print("congrats")