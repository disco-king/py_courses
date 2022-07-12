from copy import deepcopy
from classes import run_test


class CyclicIterator:
    def __init__(self, iterable):
        """ Инициализация атрибута iterable. """
        self.iterable = [i for i in iterable]

    def __iter__(self):
        """ Сохранение итаратора от iterable в state. """
        self.state = iter(self.iterable)
        return self

    def __next__(self):
        """
        Итерирование с использованием state.
        При получении StopIteration значение state
        перезаписывается значением iter(iterable).
        """
        try:
            return next(self.state)
        except StopIteration:
            self.__iter__()
            return next(self.state)


if __name__ == '__main__':

    run_test(CyclicIterator)
