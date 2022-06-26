from math import prod
from itertools import combinations_with_replacement as combs


def count_find_num(primesL, limit):
    ret = []
    if not primesL or limit < 0:
        return ret
    step = prod(primesL)
    next_step = True
    places = 1
    factor_limit = limit // step
    if factor_limit:
        ret.append(step)
    while next_step:
        next_step = False
        comb_gen = combs(primesL, places)
        for i in comb_gen:
            product = prod(i)
            if product <= factor_limit:
                ret.append(product * step)
                next_step = True
        places += 1
    return [len(ret), max(ret)] if ret else []


if __name__ == "__main__":
    print(count_find_num([], 100))
    print(count_find_num([2, 3, 5], 0))
    print(count_find_num([2, 3, 5], -1))
    print(count_find_num([127, 137, 337], 25923620897089))

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
    
