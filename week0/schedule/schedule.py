from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:

        def date_gen(date):
            ptr = date[0]
            while ptr <= date[1]:
                yield ptr
                ptr += timedelta(days=1)

        return (date
                for date_range in self.dates
                for date in date_gen(date_range))


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)