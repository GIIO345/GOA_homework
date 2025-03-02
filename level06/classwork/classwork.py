#მომხარებელს შემოატანინეთ რაიმე რიცხვი, შემდეგ for ციკლის გამოყენებით შეამოწმეთ, არის თუ არა ეს რიცხვი მარტივი, თუ არის დაპრინტეთ "your number is a prime" თუ არ არის დაპრინტეთ "your number is not a prime" 
number=int(input("enter number"))

for x in range (number):
   
 if x%1 and x:
        print("your number is a prime")
 else:
     print("invalid")