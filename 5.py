def count_find_num(primesL, limit):
    res = []
    start = 1
    for i in primesL:
        start *= i

    if start > limit:
        return []
    else:
        res.append(start)

    for j in primesL:
        for num in res:
            num *= j
            while num <= limit and num not in res:
                res.append(num)
                num *= j
    res = [len(res), max(res)]
    return res


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []