from typing import Union
from media import TV, NewsPaper
from heroes import Superman, ChuckNorris, SuperHero
from places import Place, Kostroma, Tokyo, Jupiter

# Логичнее во второй аннотации дать
# общий для всех мест абстрактный класс Place
def save_the_place(hero: SuperHero, place: Place):
    """
    Функция принимает героя и место, которое тот должен спасти.
    Герой ищет в месте противника, использует все доступные атаки,
    а потом сообщает через СМИ об очередной победе.
    """
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    hero.create_news(place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(SuperHero('Chack Norris', False), Tokyo())

    print('\n', '+' * 20, '\n', sep='')

    # Создаем героя нового класса c уникальными свойствами.
    # Кроме того, теперь мы можем прославить героя без его участия -
    # в этом помогут методы классов Media, NewsPaper и TV.

    hero = ChuckNorris()
    place = Jupiter()
    save_the_place(hero, place)
    NewsPaper.make_news(hero, place)
