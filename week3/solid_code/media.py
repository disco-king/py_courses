

class Media:

    @classmethod
    def make_news(cls, hero, place):
        place_name = getattr(place, 'name', 
                            getattr(place, 'coordinates', 'place'))
        print(f'{hero.name} saved the {place_name}!')


class TV(Media):

    @classmethod
    def make_news(cls, hero, place):
        print('TV report: ', end='')
        super(TV, cls).make_news(hero, place)


class NewsPaper(Media):

    @classmethod
    def make_news(cls, hero, place):
        print('Newspaper article: ', end='')
        super(NewsPaper, cls).make_news(hero, place)