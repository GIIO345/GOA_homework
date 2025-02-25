#1) for ციკლის გამოყენებით გამოიტანეთ რიცხვები 1-დან 10-მდე
for _ in range(10):
    print(_)
#2)for ციკლის გამოყენებით გამოიტანეთ რიცხვები 5-დან 25-მდე
for _ in range(5,25):
    print(_)

#3)for ციკლის გამოყენებით გამოიტანეთ რიცხვები 10-დან 100-მდე, 5ის stepით
for _ in range(10,100,5):
    print(_)

#4)მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა, შემდეგ ამ სიტყვიდან გამოიტანეთ მხოლოდ 'A' ასოები, თუ არ შეიცავს 'A'ს გამოიტანეთ ცარიელი სტრინგი
word=input("enter any word")
for _ in word:
    if _==("A"):
        print(_)
else:
    print(" ") #pass 
#5)კომენტარებით დაწერეთ რას გამოიტანს შემდეგი გამოსახულება: True or True and False or True and False and False and True or False
#true or true=true 
#true and false=true 
#false and false=true 
#true or false=true 
#true and true and true and true =true
