# შექმენით manual split ფუნქცია.

# def manual_split(text, delimiter):
#     lst = []
#     current = ""

#     for i in text:
#         if i == delimiter:
#             lst.append(current)
#             current = ""
#         else:
#             current += i

#     # დაამატე ბოლო ნაწილი
#     lst.append(current)
#     return lst
# print(manual_split("heloo la dao f"," "))



# def sum_str(a, b):
#     a = int(a) if a else 0
#     b = int(b) if b else 0
#     return str(a + b)



# def problem(a):
#     if a==str(a):
#         return "Error"
#     else:
#         return a*50+6


# def get_count(sentence):
#     a="aeiou"
#     return sum(1 for i in sentence if i in a)

# def delete_nth(lst, n):
#     result = []
#     for i in lst:
#         if result.count(i) < n:
#             result.append(i)
#     return result
