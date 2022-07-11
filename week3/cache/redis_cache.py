import redis


def cache_decorator(f, verbose=False):
    """
    Функция принимает в качестве аргумента
    декорируемую функцию, а возвращает объект
    функции - результата декорирования.
    Второй, опциональный аргумент - булево значение,
    определяющее, будет ли возвращаемая функция
    выводить диагностические сообщения.
    """
    try:
        # Пробуем подключиться к БД,
        # проверяем подключение с помощью ping.
        r = redis.Redis()
        r.ping()
    except:
        print('Нет доступа к Redis')
        return None

    # Кэшируемые данные хранятся в БД
    # в объекте с типом данных hash.
    # Присвоим объекту уникальное имя.
    rid = id(r)
    hash_name = f'mul_hash:{rid}'

    # Позже удалим хэш, чтобы не засорять БД.
    global name
    global redis_connection
    name = hash_name
    redis_connection = r

    def wrapper(num: int) -> int:
        """
        Функция повторяет сигнатуру функции
        multiplier, принимая int и возвращая
        аргумент, помноженный на 2.
        Если аргумент отсутствует в кэше,
        декорируемая функция выполняется,
        а результат кэшируется, в противном случае
        результат извлекается из БД
        и конвертируется в int.
        """
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

# Используем более эксплицитный способ декорирования,
# чтобы передать True в качестве значения verbose.
multiplier = cache_decorator(multiplier, True)


if __name__ == '__main__':

    # Если подключиться к серверу Redis не удалось,
    # завершаем работу скрипта.
    if not multiplier:
        exit(1)

    print(
        '\nУмножаем int на 2.\n'
        'При первом вызове с аргументом X\n'
        'функция печатает ВЫЗОВ, при повторном - КЭШ:\n')
    print(multiplier(1))
    print(multiplier(15))
    print(multiplier(-89))
    print(multiplier(3000))
    print(multiplier(1))
    print(multiplier(15))
    print(multiplier(-89))
    print(multiplier(3000))

    print()
    # Чистим БД.
    redis_connection.delete(name)
