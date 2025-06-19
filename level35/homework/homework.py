# #"გადათარგმნეთ" ფსევდო კოდი Python-ზე.

# age=int(input("enter your age: "))
# while age<18:
#     age=int(input("enter your age: "))
#     if age>18:
#         print("acces granted")





#2 დაწერეთ/ახსენით სამივე გზით ეს kata.

# def remove_smallest(numbers):
#     if not numbers:
#             return []
#     nums=numbers.copy()
#     nums.remove(min(nums))
#     return nums

#starts--> chesks list--> if  empty-- returns empty list--> if list True--> makes a copy of original string --> removes the smallest number in the copy list--> returns new list "nums"

# Checks if the list is empty. If it is, returns an empty list [] and ends the function.
# Otherwise, it creates a copy of the original list and returns a new list with the smallest number removed.

# def remove_smallest(numbers):
#     a = numbers[:]
#     if a:
#         a.remove(min(a))
#     return a
#does the same 

#4 
#sequencing runing code in order line by line 
#selection making disions in your code based on particular conditions 
#iteration reapting a block of code multiple times