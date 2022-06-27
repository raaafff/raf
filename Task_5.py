import math, itertools

def count_find_num(primesL, limit):
    minm = 1
    for num in primesL:
        minm = minm * num
    degree_list = []
    for num in primesL:
        degree_list.append(
            [num ** x for x in range(1, math.floor(
                math.log(limit / (minm / num), num)) + 1)])
    degree_tuples = list(itertools.product(*degree_list))
    result = []
    for tup in degree_tuples:
        m = 1
        for num in tup:
            m = m * num
        if m <= limit:
            result.append(m)
    if len(result):
        return [len(result), max(result)]
    return []


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
