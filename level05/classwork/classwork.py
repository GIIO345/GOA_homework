#1)for ციკლით გადაუარეთ რიცხვებს 2-დან 25-მდე და გამოიტანეთ მხოლოდ კენტი რიცხვები
for ricxvi in range(2,25):
    if ricxvi%2==1:
        print(ricxvi)

#)მომხმარებელს შემოატანინეთ სახელი inputის დახმარებით, შემდეგ for ციკლით გადაუარეთ ამ სახელს და გამოიტანეთ თვითოეული ასო ცალ-ცალკე
name=input("enter name")
for i in  name:
    print(i)

#3) შექმენით correct_password ცვლადი სადაც შეინახავთ რაიმე პაროლს, შემდეგ მომხმარებელს inputით შემოატანინეთ რაიმე პაროლი, სანამ ეს მომხმარებლის შემოტანილი პაროლი არ უდრის correct_passwordს თავიდან შემოატანინეთ მომხმარებელს პაროლი

correct_password=(333)
password=int(input("enter password"))
while correct_password!=password:
    password=int(input("enter password"))
