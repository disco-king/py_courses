from itertools import combinations 

EXAMPLE = ["b", "a", "n", "a", "n", "a"]


def bananas(s) -> set:
    result = set()
    combs = combinations(range(len(s)), 6)
    for item in combs:
        buff = [s[i] for i in item]
        if buff == EXAMPLE:
            pos = 0
            for i in range(len(s)):
                if pos < 6 and i == item[pos]:
                    pos += 1
                else:
                    buff.insert(i, "-")
            result.add("".join(buff))
    return result


#if __name__ == "__main__":
    print(bananas("bbananana"))

    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {
        "b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
        "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
        "-ban--ana", "b-anana--"
        }
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {
        "ban--ana", "ba--nana", "bana--na",
        "b--anana", "banana--", "banan--a"
        }
