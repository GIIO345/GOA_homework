#შემოატანინეთ მომხმარებელს თავისი ასაკი და შეამოწმეთ, თუ ის 10-წლისაა ან უფრო პატარა, დაპრინტეთ "Kid", თუ 10-ზე მეტი და 18-ზე ნაკლები გამოიტანეთ "teenager", თუ 18-ზე მეტია და 30-ზე ნაკლები "adult", სხვა შემთხვევაში "unc"

age=(input("enter your age: "))
if age <=10:
    print("kid")
elif age >10 and age <18:
    print("teenager")
elif age >=18 and age <30:
    print("adult")
else:
    print("unc")

#kata1
def count_positives_sum_negatives(arr):
    if not arr:
        return []

    pss = 0
    neg = 0

    for num in arr:
        if num > 0:
            pss += 1
        elif num < 0:
            neg += num

    return [pss, neg]


#kata 2
def is_opposite(s1,s2):
    if s1=="" and s2=="":
            return False
    for i in s1 :
        for q in s2:
            
            return i!=q
        

#kata 3
def monkey_count(n):
    il=[]
    for i in range (1,n+1):
        il.append(i)
    return il