#kata 1
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
def is_vow(inp):
    rel = []
    for i in inp:
        if chr(i) in "aeiou":
            rel.append(chr(i))
        else:
            rel.append(i)
    return rel
#kata 3
def monkey_count(n):
    il=[]
    for i in range (1,n+1):
        il.append(i)
    return il