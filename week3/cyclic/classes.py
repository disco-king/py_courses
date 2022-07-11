
class Range:

    def __init__(self, limit: int):
        """ Инициализация атрибутов класса. """
        self.count = 0
        self.state = 0
        self.limit = limit

    def __iter__(self):
        """ Создание и возврат класса-итератора. """
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
