import typing
from places import Place

class AntagonistFinder:

    # Аннотация типа во втором аргументе задает требования,
    # которым должен соответствовать передаваемый объект.
    def get_antagonist(self, place: Place):
        """
        Метод получает в качетве аргумента
        объект типа Place и вызывает его метод get_enemy.
        Ничего не возвращает.
        """
        place.get_enemy()
