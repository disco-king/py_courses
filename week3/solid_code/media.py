from abc import ABC, abstractmethod
from heroes import SuperHero
from places import Place

# Абстрактный класс Media имплементируют
# потомки, дополнив функционал метода make_news
# и определив абстрактный метод denote_medium.

class Media(ABC):

    def make_news(self, hero: SuperHero, place: Place):
        """
        Метод получает в качестве аргументов героя и место,
        объявляет о спасении места героем. Ничего не возвращает
        """
        place_name = place.get_location()
        hero_name = hero.get_name()
        self.denote_medium()
        print(f'{hero_name} saved the {place_name}!')

    @abstractmethod
    def denote_medium(self):
        """
        Метод объявляет, какое именно СМИ сообщает новость.
        Ничего не принимает и не возвращает.
        """
        pass


class TV(Media):

    def denote_medium(self):
        print('TV report:', end=' ')


class NewsPaper(Media):

    def denote_medium(self):
        print('TV report:', end=' ')
