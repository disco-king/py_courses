from typing import Union
from media import TV, NewsPaper
from heroes import Superman, ChuckNorris, SuperHero
from places import Kostroma, Tokyo


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo]):
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

    hero = ChuckNorris()
    place = Tokyo()
    save_the_place(hero, place)
    TV.make_news(hero, place)
    NewsPaper.make_news(hero, place)
