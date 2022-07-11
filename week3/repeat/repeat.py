import time

class RepeatDecorator:

    def __init__(self, count: int, start_sleep_time: float,
                    factor: int, border_sleep_time: float):
        """ Инициализация атрибутов параметрами init. """
        self.count = count
        if start_sleep_time > border_sleep_time:
            self.pause = border_sleep_time
        else:
            self.pause = start_sleep_time
        self.factor = factor
        self.border_time = border_sleep_time

    def __call__(self, func):
        """
        Магический метод, позволяющий вызвать класс как функцию.
        Возвращает функцию-аргумент, "обернутую" во wrapper.
        """
        def wrapper(*args, **kwargs):
            """
            Функция-обертка, выставляющая паузы для основной фунции.
            Вызов основной функции производится через
            экспоненциально увеличивающиеся промежутки времени.
            При этом пауза перед первым вызовом
            и после последнего вызова отсутствует.
            """
            start = time.perf_counter()
            func()
            for i in range(self.count - 1):
                print("Пауза:", self.pause)
                time.sleep(self.pause)
                curr = time.perf_counter()
                print("Время (сек) с начала работы:", curr - start)
                self._update_sleep_time()
                func()

        return wrapper

    def _update_sleep_time(self):
        """
        Обновление времени ожидания.
        Если время ожидания превысило лимит,
        ему присвается значение лимита.
        """
        if self.pause < self.border_time:
            self.pause *= 2 ** self.factor
        if self.pause > self.border_time:
            self.pause = self.border_time


@RepeatDecorator(5, 1, 1, 10)
def func():
    print("<<< func called >>>")

if __name__ == "__main__":
    print("5 вызовов, неограниченный рост до 8 сек.:")
    func()
    print()

    print("3 вызова, неограниченный рост до 6 сек.:")
    @RepeatDecorator(3, 3, 1, 20)
    def func():
        print("<<< func called >>>")
    func()
    print()

    print("4 вызова, рост ограничен"
            " значением в 3 сек. на втором вызове:")
    @RepeatDecorator(4, 2, 5, 3)
    def func():
        print("<<< func called >>>")
    func()
    print()

    print("4 вызова, рост отсутствует:")
    @RepeatDecorator(4, 1, 0, 100)
    def func():
        print("<<< func called >>>")
    func()

