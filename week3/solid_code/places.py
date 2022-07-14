from abc import ABC, abstractmethod

# С помощью абстрактного класса задаем формальные требования
# для всех классов-потомков, а именно - необходимость
# определить методы get_location и get_enemy, используемыe другими классами.

class Place(ABC):

    @abstractmethod
    def get_enemy(self):
        """
        Метод определяет, где именно находятся враги.
        Выводит местонахождение в STDOUT, ничего не возвращая.
        """
        pass

    @abstractmethod
    def get_location(self):
        """
        Метод определяет, как именно назвать спасенное место.
        Ничего не принимает, возвращает необходимую информацию. 
        """
        pass


class Kostroma(Place):
    city_name = 'Kostroma'

    def get_enemy(self):
        print('Orcs hid in the forest')
    
    def get_location(self):
        return self.city_name 



class Tokyo(Place):
    name = 'Tokyo'

    def get_enemy(self):
        print('Godzilla stands near a skyscraper')

    def get_location(self):
        return self.name 


class Jupiter(Place):
    coordinates = [1234.5678, 8765.4321]

    def get_enemy(self):
        print('Death star floats around in space')

    def get_location(self):
        return self.coordinates 


