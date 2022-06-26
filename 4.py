from itertools import combinations


def bananas(s):
    res = set()
    if len(s) < 6:
        return res

    if len(s) == 6 and s == "banana":
        res.add(s)
        return res

    char_combinations = combinations(range(len(s)), 6)

    for comb in char_combinations:
        list_comb = list(comb)

        tmp_string = ''
        arr_t = ['-'] * len(s)

        for i in list_comb:
            arr_t[i] = s[i]
            tmp_string += s[i]

        res_string = ''.join(arr_t)
        if tmp_string == 'banana':
            res.add(res_string)

    return res


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}