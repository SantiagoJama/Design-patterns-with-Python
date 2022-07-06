from Structural.Decorator.Hero import Hero
from abc import abstractmethod


class HeroDecorator(Hero):

    def __init__(self):
        print("Hero decorator")

    @abstractmethod
    def use_special_power(self):
        pass



