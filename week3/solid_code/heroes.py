from antagonistfinder import AntagonistFinder
from media import Media, TV


# В каждом настоящем герое множество талантов.
# Предоставляем на выбор cтрелка, cверхчеловека
# и мастера единоборств.

class Shooter:
    def fire_a_gun(self):
        """
        Метод производит звук выстрела.
        Ничего не принимает и не возвращает.
        """
        print('PIU PIU')


class SuperHuman:
    def incinerate_with_lasers(self):
        """
        Метод производит звук пальбы лазером из глаз.
        Ничего не принимает и не возвращает.
        """
        print('Wzzzuuuup!')


class KarateMaster:
    def roundhouse_kick(self):
        """
        Метод производит звук удара.
        Ничего не принимает и не возвращает.
        """
        print('Bump')


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        """
        Метод присваивает атрибутам name и
        can_use_ultimate_attack значения поступивших параметров.
        Определения атрибутов finder и Media от параметров
        не зависят и определяются одинаково для каждого объекта класса.
        """
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()
        self.media = Media()

    def find(self, place):
        """
        Метод вызывает метод get_antagonist объекта finder
        с параметром place. Ничего не возвращает.
        """
        self.finder.get_antagonist(place)

    # Делегируем создание новостей классу Media.
    # Наследники Media имеют такую же
    # сигнатуру метода make_news, и потому
    # взаимозаменяемы с родителем (см. ChuchNorris ниже).
    def create_news(self, place):
        """
        Метод вызывает метод get_antagonist объекта media
        с параметром place. Ничего не возвращает.
        """
        self.media.make_news(self, place)

    # Задаем для "типичного" героя атаку-болванку.
    # Каждый из героев-наследников этого класса может
    # переопределить ее, используя классы-миксины.
    def attack(self):
        """
        Метод производит звук атаки.
        Ничего не принимает и не возвращает.
        """
        print('*Generic attack sound*')

    # То же, что и с обычной атакой.
    def ultimate(self):
        """
        Метод производит звук особой атаки.
        Ничего не принимает и не возвращает.
        """
        print('*Generic ultimate attack sound*')


class Superman(SuperHero, SuperHuman, KarateMaster):

    def __init__(self):
        """ Метод инициализирует объект базового класса. """
        super(Superman, self).__init__('Clark Kent', True)

    # Сохраняем сигнатуру родителя, но используем 
    # миксины для переопределения обеих атак.

    def attack(self):
        """
        Метод переопределяет атаку базового класса
        с помощью метода класса-миксина.
        """
        self.roundhouse_kick()

    def ultimate(self):
        """
        Метод переопределяет особую атаку базового класса
        с помощью метода класса-миксина.
        """
        self.incinerate_with_lasers()


class ChuckNorris(SuperHero, Shooter, KarateMaster):

    # Чак - телезвезда, поэтому гораздо уместнее
    # дать ему рассказать о своих достижениях по TV.
    # Хорошо, что подстановка по Барбаре Лисков
    # позволяет это сделать без дополнительных усилий.

    def __init__(self):
        """
        Метод инициализирует объект базового класса.
        Атрибут media переопределяется
        в соответствии со спецификой класса. 
        """
        super(ChuckNorris, self).__init__('Chuck Norris', True)
        self.media = TV()

    # Хотя Чак - тоже своего рода Супермен,
    # атаки у него должны быть другие.
    def attack(self):
        """
        Метод переопределяет атаку базового класса
        с помощью метода класса-миксина.
        """
        self.roundhouse_kick()

    def ultimate(self):
        """
        Метод переопределяет особую атаку базового класса
        с помощью метода класса-миксина.
        """
        self.fire_a_gun()
