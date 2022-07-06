from Structural.Decorator.HeroDecorator import HeroDecorator
from Structural.Decorator.Hero import Hero


class Shield(HeroDecorator):

    def __init__(self, hero: Hero):
        print("The Shield")
        self.__hero = hero

    def use_special_power(self):
        return f'{self.__hero.defend()}, but now I\'m using {self.__use_a_platinum_shield()}'

    def __use_a_platinum_shield(self):
        return f'the platinum shield'
