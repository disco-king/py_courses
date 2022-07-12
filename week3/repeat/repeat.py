import time

class RepeatDecorator:

    def __init__(self, count: int, start_sleep_time: float,
                    factor: int, border_sleep_time: float):
        """ Инициализация атрибутов параметрами init. """
        self.count = count
        if start_sleep_time > border_sleep_time:
            self.sleep_time = border_sleep_time
        else:
            self.sleep_time = start_sleep_time
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
            print("Количество запусков: ", self.count)
            print("Начало работы")

            for i in range(1, self.count + 1):
                res = func(*args, **kwargs)
                time.sleep(self.sleep_time)
                print(f"Запуск номер {i}. Ожидание: {self.sleep_time} сек."
                        f" Результат декорируемой функции: {res}")
                self._update_sleep_time(i)

            print("Конец работы")

        return wrapper

    def _update_sleep_time(self, iteration):
        """
        Обновление времени ожидания.
        Если время ожидания превысило лимит,
        ему присвается значение лимита.
        """
        if self.sleep_time < self.border_time:
            self.sleep_time *= self.factor ** iteration
        if self.sleep_time > self.border_time:
            self.sleep_time = self.border_time


@RepeatDecorator(5, 1, 2, 10)
def func(num: int) -> int:
    return num + num

if __name__ == "__main__":
    func(2)


