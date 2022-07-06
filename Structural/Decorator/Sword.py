from Structural.Decorator.HeroDecorator import HeroDecorator
from Structural.Decorator.Hero import Hero

class Sword(HeroDecorator):

    def __init__(self, hero: Hero):
        print("The gold Sword")
        self.__hero = hero

    def use_special_power(self):
        return f'{self.__hero.fight()}, but now I\'m using {self.__use_a_gold_sword()}'

    def __use_a_gold_sword(self):
        return f'the gold sword'


