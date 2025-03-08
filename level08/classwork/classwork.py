#1) მომხმარებელს შემოატანინეთ სიტყვა ან წინადადება შეინახეთ ის შეტრიალებულად reversed_string  ცვლადში და გამოიტანეთ ეს ცვლადი
word=input("enter a word")
reversed_string=word[::-1]
print(reversed_string)
#2) გამოთვალეთ 0 დან 100ს ჩათვლით ყველა რიცხვის ჯამი და შეინახეთ ის sum ცვლადში
count=0
for i in range(0,100):
    count+=i
    sum=count
    print(sum)

#3) მომხმარებეს შემოატანინეთ სამ ასოიანი სიტყვა, თუ  მან არ შემოიყვანა სამი ასო მაშინ გამოუპრინტეთ რომ მან უნდა შეიყვანოს ზუსტად სამი ასო და გაუშვას პროგრამა თავიდან. როდესაც მომხმარებელი შეიყვანს სამ ასოიან სიტყვას, შეამოწმეთ არის თუ არა ის პალინდრომი და გაოუტანეთ True ან False შესაბამისად
Word=input("enter a word")
while len(Word) < 3:
    print("word must contain three character ")
    Word=input("enter a word")
if Word==Word[::-1]:
    print("True")
else:
    print("False")

#4) გამოიტანეთ 100დან 300მდე ყველა რიცხვის კვადრატი 
for i in range(100,300):
    print(i*i)

#5) გამოიტანეთ ჯერ False, შემდეგ True, შემდეგ False, True, False... და ასე 1000-ჯერ
T=("True")
print(T)
F=("False")
print(F)
for i in range(1000):
    print(T)
    print(F)

#6)BONUS ) მომხმარბელს შემოყავს N-ინტეჯერი, იპოვეთ N-ის ფესვი, თუ ვერ იპოვეთ გამოიტანეთ false
N=int(input("enter a number"))
root=N**0.5
if root*root!=N:
    print("False")
    
