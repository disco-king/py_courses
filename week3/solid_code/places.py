from abc import ABC, abstractmethod


class Place(ABC):

    @abstractmethod
    def get_enemy(self):
        pass


class Kostroma(Place):
    city_name = 'Kostroma'

    def get_enemy(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def get_enemy(self):
        print('Godzilla stands near a skyscraper')
