
class Range:

    def __init__(self, limit: int):
        """ Инициализация атрибутов класса. """
        self.limit = limit

    def __iter__(self):
        """ Создание и возврат класса-итератора. """
        self.state = 0
        return Iterator(self)

class Iterator:

    def __init__(self, obj):
        """ Инициализация атрибута класса. """
        self.obj = obj

    def __next__(self):
        """
        Переменная state инкрементируется
        и возвращается до тех пор, пока
        не станет больше лимита или равна ему.
        """
        if self.obj.state >= self.obj.limit:
            raise StopIteration
        ret = self.obj.state
        self.obj.state += 1
        return ret


class Range2:
    def __init__(self, stop_value: int):
        """ Инициализация атрибутов класса. """
        self.current = -1
        self.stop_value = stop_value - 1

    def __iter__(self):
        """
        Так как класс выполняет функции
        и итерируемого объекта, и итератора,
        в качестве итератора он возвращает сам себя.
        """
        self.current = -1
        return self

    def __next__(self):
        """
        Переменная state инкрементируется
        и возвращается до тех пор, пока
        не станет больше лимита или равна ему.
        """
        if self.current < self.stop_value:
            self.current += 1
            return self.current
        raise StopIteration


def get_obj(code):
    if code == 0:
        obj = range(3)
    elif code == 1:
        obj = [0, 1, 2]
    elif code == 2:
        obj = (0, 1, 2)
    elif code == 3:
        obj = {0, 1, 2}
    elif code == 4:
        obj = '012'
    elif code == 5:
        obj = Range(3)
    elif code == 6:
        obj = Range2(3)
    elif code == 7:
        print('[list with one item] ', end='')
        obj = [-1]
    elif code == 8:
        print('[empty list] ', end='')
        obj = []
    return obj

def run_test(Class):
    for code in range(9):

        count = 0
        obj = get_obj(code)
        it = Class(obj)
        print(type(obj))

        print('while loop:\t', end='')
        it = iter(it)
        while True:
            if count >= 10:
                break
            try:
                print(next(it), end=' ')
                count += 1
            except StopIteration:
                break
        print()

        count = 0

        print('for loop:\t', end='')
        for i in it:
            if count >= 10:
                break
            print(i, end=' ')
            count += 1
        print()

        print()