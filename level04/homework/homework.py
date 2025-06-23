
#1. შექმენით პროგრამა სადაც მომხმარებელი შემოიყვანს ასაკს და თქვენ უნდა გაარკვიოთ, უნდა იაროს მან ბაღში, სკოლაში თუ სამსახურში: თუ ასაკი მეტი იქნება 2-ზე == ბაღი | თუ ასაკი მეტია ან უდრის 6-ს == სკოლაში | დანარჩენ შემთხვევაში სამსახური. (edited)
AGe=int(input("enter your age"))
if AGe>=6:
    print("you should be in school")
elif AGe>2:
    print("you should be in kindergarten")
else:
    print("you should be employed")

#2. შექმენით პროგრამა რომელშიც: მომხმარებელს შემოყავს ინფორმაცია თუ რომელ პროგრამირების  აკადემიაში დადის, თუ მან შეიყვანა "Goa", გამოიტანეთ "U r a real chad!", ხოლო დანარჩენ შემთხვევაში "Join Goa, become a chad".
academy=input("which academy are you going to")
if academy=="Goa":
    print("U r a real chad!")
else:
    print("Join Goa, become a chad")

#3. მომხმარებელს შემოყავს პროექტში მიღებული ქულის შესახებ, თუ ის 90-ზე მეტია შეფასებაა A, თუ 75-ზე მეტია შეფასებაა B, თუ 60-ზე მეტია შეფასებაა C, თუ 50-ზე მეტია შეფასებაა D, თუ 40-ზე E და თუ 30-ზე F, Good Luck 
grade=int(input("enter your current grade"))
if grade>90:
    print("A")
elif grade>75:
    print("B")
elif grade>60:
    print("C")
elif grade>50:
    print("D")
elif grade>40:
    print("E")
elif grade > 30:
    print("F")
else:
    print("you have failed")

