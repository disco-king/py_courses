from abc import ABC, abstractmethod
from typing import List

# С помощью абстрактного класса задаем формальные требования
# для всех классов-потомков, а именно - необходимость
# определить метод get_enemy, используемый другими классами.
class Place(ABC):

    @abstractmethod
    def get_enemy(self):
        """
        Метод определяет, где именно находятся враги.
        Выводит местонахождение в STDOUT, ничего не возвращая.
        """
        pass


class Kostroma(Place):
    city_name = 'Kostroma'

    def get_enemy(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def get_enemy(self):
        print('Godzilla stands near a skyscraper')


class Jupiter(Place):
    coordinates = [1234.5678, 8765.4321]

    def get_enemy(self):
        print('Death star floats around in space')
