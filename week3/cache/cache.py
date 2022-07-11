
def cache_decorator(f, verbose=False):
    """
    Функция принимает в качестве аргумента
    декорируемую функцию, а возвращает
    функцию - результата декорирования.
    Второй, опциональный аргумент - булево значение,
    определяющее, будет ли возвращаемая функция
    выводить диагностические сообщения.
    """
    cache = {}

    def wrapper(*args, **kwargs):
        """
        Функция-обертка принимает произвольное
        количество параметров, и возвращает
        объект - результат работы декорируемой функции.
        Если функция уже вызывалась для полученных аргументов,
        значение возвращается из кэша, если нет -
        вызывается функция, а результат кэшируется.
        """
        nonlocal cache
        # В качестве ключа для словаря используется
        # представление всех аргументов функции
        # в виде строки. Таким образом хэширование возможно
        # даже для нехэшируемых типов.
        hash_val = str(args) + str(kwargs)
        signal = 'КЭШ'

        if hash_val not in cache:
            cache[hash_val] = f(*args, **kwargs)
            signal = 'ВЫЗОВ'

        if verbose:
            print(signal, end=': ')
        return cache[hash_val]

    return wrapper


@cache_decorator
def multiplier(number: int):
    return number * 2

# Еще две функции чтобы убедиться,
# что декоратор может работать с любым
# количеством и типами аргументов.
def adder(item):
    return item + item

def str_multiplier(string: str, number: int):
    return string * number

adder = cache_decorator(adder, True)
str_multiplier = cache_decorator(str_multiplier, True)

if __name__ == '__main__':

    print('\nУмножаем int на 2 (пока без комментариев):')
    print(1, ': ', multiplier(1), sep='')
    print(15, ': ', multiplier(15), sep='')
    print(-89, ': ', multiplier(-89), sep='')
    print(3000, ': ', multiplier(3000), sep='')

    multiplier = cache_decorator(multiplier, True)
    print('\nТеперь убедимся, что кэш работает.\n'
        'При первом вызове с аргументом X\n'
        'функция печатает ВЫЗОВ, при повторном - КЭШ:\n')
    print(multiplier(1))
    print(multiplier(15))
    print(multiplier(1))
    print(multiplier(-89))
    print(multiplier(15))


    print('\nРабота с другими типами данных:')

    print('\nСкладываем строки и списки сами с собой:')
    print(adder('foo'))
    print(adder('bar'))
    print(adder('foo'))
    print(adder([1, 2, 3]))
    print(adder([4, 5, 6]))
    print(adder([1, 2, 3]))

    print('\nУмножаем строки на число:')
    print(str_multiplier('yo ', 3))
    print(str_multiplier('ole ', 4))
    print(str_multiplier('yo ', 3))
