from abc import ABC, abstractmethod
from heroes import SuperHero
from places import Place

# Абстрактный класс Media имплементируют
# потомки, определяя абстрактный метод denote_medium.

class Media(ABC):

    def make_news(self, news):
        """
        Метод получает в качестве аргументов героя и место,
        объявляет о спасении места героем. Ничего не возвращает.
        """
        self.denote_medium()
        print(news)

    @abstractmethod
    def denote_medium(self):
        """
        Метод объявляет, какое именно СМИ сообщает новость.
        Ничего не принимает и не возвращает.
        """
        pass

# Выносим функционал работы с информацией в отдельный класс,
# cоблюдая принцип единой ответственности и инверсии зависимостей.
class NewsMaker:

    @staticmethod
    def get_info(hero: SuperHero, place: Place):
        """
        Метод принимает объекты типов SuperHero и Place,
        извлекает из них необходимые данные,
        и возвращает формат-строку с новостью.
        """
        place_name = place.get_location()
        hero_name = hero.get_name()
        return f'{hero_name} saved the {place_name}!'


class TV(Media):

    def denote_medium(self):
        print('TV report:', end=' ')


class NewsPaper(Media):

    def denote_medium(self):
        print('Newspaper article:', end=' ')
