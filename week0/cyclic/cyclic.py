from test import Range, Range2
from copy import deepcopy


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
    return obj


class CyclicIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)

    def __iter__(self):
        self.state = deepcopy(self.iterator)
        return self

    def __next__(self):
        try:
            return next(self.state)
        except StopIteration:
            self.__iter__()
            return next(self.state)


if __name__ == '__main__':

    for code in range(5):

        count = 0
        obj = get_obj(code)
        it = CyclicIterator(obj)
        print(type(obj))

        print('while loop:\t', end='')
        it = iter(it)
        while True:
            if count >= 10:
                break
            print(next(it), end=' ')
            count += 1
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
