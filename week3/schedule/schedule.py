import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        """
        Метод использует промежутки времени,
        хранящиеся в атрибутах класса,
        и возвращает объект-генератор,
        по очереди генерирующий даты из промежутков.
        """

        def date_gen(date):
            """
            Функция выполняет "ленивое итерирование",
            по очереди возвращая даты из промежутка,
            пока они не закончатся.
            """
            ptr = date[0]
            while ptr <= date[1]:
                yield ptr
                ptr += timedelta(days=1)

        return (date
                for date_range in self.dates
                for date in date_gen(date_range))


if __name__ == '__main__':

    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)

    if len(sys.argv) == 1 or sys.argv[1] != 'more':
        print('\nЧтобы увидеть дополнительные тесты,\n'
                'передайте скрипту аргумент more')
        exit(0)

    movies = []

    movies.append(Movie('больше промежутков, следующий месяц и год', [
        (datetime(2020, 1, 15), datetime(2020, 1, 18)),
        (datetime(2020, 5, 25), datetime(2020, 6, 3)),
        (datetime(2021, 9, 30), datetime(2021, 10, 1)),
        (datetime(2021, 12, 30), datetime(2022, 1, 3))
    ]))

    movies.append(Movie('один промежуток', [
        (datetime(2020, 7, 26), datetime(2020, 8, 2))
    ]))

    movies.append(Movie('ошибка в одном из промежутков', [
        (datetime(2020, 1, 15), datetime(2020, 1, 25)),
        (datetime(2020, 3, 7), datetime(2020, 3, 1))
    ]))

    movies.append(Movie('пустое расписание', []))

    for mov in movies:
        print(f"\n{mov.title}:\n")
        for day in mov.schedule():
            print(day)
