from test import Range, Range2
from copy import deepcopy

class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        self.state = iter(self.iterable)
        return self

    def __next__(self):
        try:
            return next(self.state)
        except StopIteration:
            # print("start again")
            self.__iter__()
            return next(self.state)


count = 0


# it = CyclicIterator(range(3))
# it = CyclicIterator([0, 1, 2])
it = CyclicIterator(Range(3))
# it = CyclicIterator(Range2(3))


# while True:
#     if count >= 3:
#         break
#     print(next(it))
#     count += 1


for i in it:
    if count >= 10:
        break
    print(i)
    count += 1