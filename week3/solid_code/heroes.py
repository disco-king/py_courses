from abc import ABC, abstractmethod
from antagonistfinder import AntagonistFinder


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


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        """
        Метод присваивает атрибутам name, media и
        can_use_ultimate_attack значения поступивших параметров.
        Определения атрибутa finder от параметров
        не зависит и определяeтся одинаково для каждого объекта класса.
        """
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        """
        Метод вызывает метод get_antagonist объекта finder
        с параметром place. Ничего не возвращает.
        """
        self.finder.get_antagonist(place)

    def get_name(self):
        return self.name

    # Задаем для "типичного" героя абстрактную атаку.
    # Каждый из героев-наследников этого класса
    # должен будет определить ее, используя классы-миксины.
    @abstractmethod
    def attack(self):
        """
        Метод издает звук атаки.
        Ничего не принимает и не возвращает.
        """
        pass

    # То же, что и с обычной атакой.
    @abstractmethod
    def ultimate(self):
        """
        Метод издает звук особой атаки.
        Ничего не принимает и не возвращает.
        """
        pass


class Superman(SuperHero, SuperHuman, KarateMaster):

    def __init__(self):
        """ Метод инициализирует объект базового класса. """
        super(Superman, self).__init__('Clark Kent', True)

    # Сохраняем сигнатуру родителя, используем 
    # миксины для определения обеих атак.

    def attack(self):
        """
        Метод определяет атаку базового класса
        с помощью метода класса-миксина.
        """
        self.roundhouse_kick()

    def ultimate(self):
        """
        Метод определяет особую атаку базового класса
        с помощью метода класса-миксина.
        """
        self.incinerate_with_lasers()


class ChuckNorris(SuperHero, Shooter, KarateMaster):

    def __init__(self):
        """
        Метод инициализирует объект базового класса.
        Атрибут media переопределяется
        в соответствии со спецификой класса. 
        """
        super(ChuckNorris, self).__init__('Chuck Norris', True)

    # Хотя Чак - тоже своего рода Супермен,
    # атаки у него должны быть другие.
    def attack(self):
        """
        Метод определяет атаку базового класса
        с помощью метода класса-миксина.
        """
        self.roundhouse_kick()

    def ultimate(self):
        """
        Метод определяет особую атаку базового класса
        с помощью метода класса-миксина.
        """
        self.fire_a_gun()


class YoungJedi(SuperHero, SuperHuman, Shooter):

    def __init__(self):
        """
        Метод инициализирует объект базового класса.
        Атрибут media переопределяется
        в соответствии со спецификой класса. 
        """
        super(YoungJedi, self).__init__('Luke Skywalker', False)

    def attack(self):
        """
        Метод определяет атаку базового класса
        с помощью метода класса-миксина.
        """
        self.fire_a_gun()

    def ultimate(self):
        """
        Метод определяет особую атаку базового класса
        с помощью метода класса-миксина.
        """
        self.incinerate_with_lasers()
