class Range:

    def __init__(self, limit: int):
        self.count = 0
        self.state = 0
        self.limit = limit

    def __iter__(self):
        return Iterator(self)

class Iterator:

    def __init__(self, obj):
        self.obj = obj

    def __next__(self):
        if self.obj.state >= self.obj.limit:
            raise StopIteration
        ret = self.obj.state
        self.obj.state += 1
        return ret


class Range2:
    def __init__(self, stop_value: int):
        self.current = -1
        self.stop_value = stop_value - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_value:
            self.current += 1
            return self.current
        raise StopIteration
