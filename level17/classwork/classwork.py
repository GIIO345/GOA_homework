#შექმენით manual_sum ფუნქცია


list=[23,5,4,32,23,5,2,]
def manual_sum(l):
    count=0
    for i in list:
        count+=i
    return count
print(manual_sum(list))



#შექმენით manual_append ფუნქცია
numbers=[23,5,4,32,23,5,2,]
k=int(input("enter a number"))
def func(numbers,k):
    res=numbers+[k]
    return res
print (func(numbers,k))


