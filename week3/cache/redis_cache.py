import redis


def cache_decorator(f, verbose=False):

    r = redis.Redis()
    if not r.ping():
        print('нет доступа к redis')
        return None

    rid = id(r)
    hash_name = f'mul_hash:{rid}'

    # позже удалим хэш, чтобы не засорять БД
    global name
    global redis_connection
    name = hash_name
    redis_connection = r

    def wrapper(num: int) -> int:
        nonlocal r

        if not r.hexists(hash_name, num):
            res = f(num)
            r.hset(hash_name, num, res)
            signal = 'ВЫЗОВ'
        else:
            res = int(r.hget(hash_name, num).decode('utf-8'))
            signal = 'КЭШ'

        if verbose:
            print(signal, end=': ')
        return res

    return wrapper


def multiplier(number: int):
    return number * 2

multiplier = cache_decorator(multiplier, True)

if __name__ == "__main__":

    print(
        '\nУмножаем int на 2.\n'
        'При первом вызове функция печатает ВЫЗОВ,\n'
        'При повторном - КЭШ:\n')
    print(multiplier(1))
    print(multiplier(15))
    print(multiplier(3000))
    print(multiplier(-89))
    print(multiplier(1))
    print(multiplier(15))
    print(multiplier(-89))
    print(multiplier(3000))

    print()
    print(name)
    # чистим БД
    # redis_connection.delete(name)
    print("результат удаления: ", redis_connection.delete(name))
