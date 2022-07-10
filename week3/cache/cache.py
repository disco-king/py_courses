
def cache_decorator(f, verbose=False):
    cache = {}

    def wrapper(*args, **kwargs):
        nonlocal cache
        hash_val = hash(str(args) + str(kwargs))
        signal = "КЭШ"

        if hash_val not in cache:
            cache[hash_val] = f(*args, **kwargs)
            signal = "ВЫЗОВ"

        if verbose:
            print(signal, end=': ')
        return cache[hash_val]

    return wrapper


@cache_decorator
def multiplier(number: int):
    return number * 2

def adder(item):
    return item + item
adder = cache_decorator(adder, True)

def str_multiplier(string: str, number: int):
    return string * number
str_multiplier = cache_decorator(str_multiplier, True)

if __name__ == "__main__":

    print('\nумножаем int на 2 (пока без комментариев):')
    print(1, ': ', multiplier(1), sep='')
    print(15, ': ', multiplier(15), sep='')
    print(-89, ': ', multiplier(-89), sep='')
    print(3000, ': ', multiplier(3000), sep='')

    multiplier = cache_decorator(multiplier, True)
    print('\nтеперь убедимся, что кэш работает:')
    print(multiplier(1))
    print(multiplier(15))
    print(multiplier(1))
    print(multiplier(-89))
    print(multiplier(15))


    print('\nработа с другими типами данных'
            ' и комментариями для наглядности:')

    print('\nскладываем строки и списки сами с собой:')
    print(adder("foo"))
    print(adder("bar"))
    print(adder("foo"))
    print()
    print(adder([1, 2, 3]))
    print(adder([4, 5, 6]))
    print(adder([1, 2, 3]))

    print('\nумножаем строки на число:')
    print(str_multiplier("yo", 3))
    print(str_multiplier("ole", 3))
    print(str_multiplier("yo", 3))
