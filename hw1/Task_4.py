import itertools

def bananas(s) -> set:
    res = set()
    for comb in itertools.combinations(range(len(s)), len(s) - len('banana')):
        sep = list(s)
        for i in comb:
            sep[i] = '-'
        med_res = ''.join(sep)
        if med_res.replace('-', '') == 'banana':
            res.add(med_res)
    return res


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
