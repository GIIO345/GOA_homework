def sum_array(a):
    if a=="":
        return "0"
    else:
        return sum(i for i in a)
    


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


def accum(st):
    result = []
    for i in range(len(st)):
        letter = st[i]
        part = letter.upper() + letter.lower() * i
        result.append(part)
    return "-".join(result)