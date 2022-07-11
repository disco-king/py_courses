from antagonistfinder import AntagonistFinder
from media import Media

class Shooter:

    def fire_a_gun(self):
        print('PIU PIU')


class SuperHuman:

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class KarateMaster:

    def roundhouse_kick(self):
        print('Bump')


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()
        self.media = Media()

    def find(self, place):
        self.finder.get_antagonist(place)

    # Проблема: Герой не должен заниматься оповещениями о своей победе, это задача масс-медиа.
    # Несоблюден: Принцип единой ответственности.
    # По SOLID: Вынести оповещение в отдельный класс, занимающийся выводом информации.
    # Когда возникнут трудности? Добавьте оповещение о победе героя через газеты или через TV (на выбор)
    # а также попробуйте оповестить планеты (у которых вместа атрибута name:str используется coordinates:List[float]).
    def create_news(self, place):
        self.media.make_news(self, place)

    # Проблема: Для каждого супергероя реализованы все методы обращения с оружием.
    # Несоблюден: Принцип разделения интерфейса
    # По SOLID: Создать классы-миксины для каждого оружия
    # Когда возникнут трудности? Попробуйте запретить Чаку норрису пользоваться лазерами из глаз!

    def attack(self):
        print('*Generic attack sound*')

    # Проблема: У разных супергероев разные суперспособности
    # Несоблюден: Принцип открытости/закрытости
    # По SOLID: Каждого супергероя реализовать как наследника SuperHero и вместо изменения базового класса переопределять нужные методы
    # Когда возникнут трудности? Когда в вашем коде поселится вся команда Мстителей
    def ultimate(self):
        print('*Generic ultimate attack sound*')


class Superman(SuperHero, SuperHuman, KarateMaster):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    # Проблема: Сигнатура метода изменилась. Если мэр города обратится к супермену как к супергерою у Кларка возникнут проблемы с атакой
    # Несоблюден: Принцип подстановки Барбары Лисков
    # По SOLID: Не допускать таких вольностей
    # Когда возникнут трудности? При первой же битве
    def attack(self):
        self.roundhouse_kick()

    def ultimate(self):
        self.incinerate_with_lasers()


class ChuckNorris(SuperHero, Shooter, KarateMaster):

    def __init__(self):
        super(ChuckNorris, self).__init__('Chuck Norris', True)

    def attack(self):
        self.roundhouse_kick()

    def ultimate(self):
        self.fire_a_gun()
