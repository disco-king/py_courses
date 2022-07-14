from media import Media, TV, NewsPaper
from heroes import SuperHero, Superman, ChuckNorris, YoungJedi
from places import Place, Kostroma, Tokyo, Jupiter

# Логичнее во второй аннотации дать
# общий для всех мест абстрактный класс Place
def save_the_place(hero: SuperHero, place: Place, media: Media):
    """
    Функция принимает героя и место, которое тот должен спасти,
    а также объект СМИ, чтобы сообщить о результате.
    Герой ищет в месте противника, использует все доступные атаки,
    а потом СМИ сообщают об очередной победе добра над злом.
    """
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    media.make_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), TV())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), NewsPaper())
    print('-' * 20)
    save_the_place(YoungJedi(), Jupiter(), TV())
