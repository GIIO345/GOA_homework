#შექმენით ფუნქცია, რომელსაც გადაეცემა შემდეგი ლისთი: [1,23,165,2,3,92,10,34,911] და ერთი ინტეჯერი(მაგ. 3), 
#თქვენი დავალებაა, რომ ახალ ცარიელ ლისთში შეინხოთ მხოლოდ ისეთი რიცხვები, რომლებიც უნაშთოთ იყოფიან გადმოცემულ ინტეჯერზე(ამ შემთხვევაში 3-ზე).
nums= [1,23,165,2,3,92,10,34,911]
num=3
res=[]

def func(nums,num):
    res=[]
    for i in (nums):
        if i%num==0:
            res.append(i)
            return res

print(func(nums,num))


def reverseList(lst):
    return lst[::-1]


def even_last(numbers): 
    if not numbers:
        return 0
    count=0
    for i in range(0,len(numbers),2):
        count+=numbers[i]
    return count*numbers[-1]