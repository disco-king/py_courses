# В дополнение к общему классу Media
# (который, кстати, поддерживает и координаты планет)
# создадим двух потомков с идентичными сигнатурами
# их classmethod'ов, чтобы любой герой мог выбрать
# СМИ себе по душе.

class Media:

    @classmethod
    def make_news(cls, hero, place):
        """
        Метод получает в качестве аргументов героя и место,
        объявляет о спасении места героем. Ничего не возвращает
        """
        place_name = getattr(place, 'name', 
                            getattr(place, 'coordinates', 'place'))
        print(f'{hero.name} saved the {place_name}!')


class TV(Media):

    @classmethod
    def make_news(cls, hero, place):
        """
        Метод изменяет функционал
        make_news базового класса.
        """
        print('TV report: ', end='')
        super(TV, cls).make_news(hero, place)


class NewsPaper(Media):

    @classmethod
    def make_news(cls, hero, place):
        """
        Метод изменяет функционал
        make_news базового класса.
        """
        print('Newspaper article: ', end='')
        super(NewsPaper, cls).make_news(hero, place)
