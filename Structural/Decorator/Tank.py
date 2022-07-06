from Structural.Decorator.Hero import Hero


class Protector(Hero):

    def __init__(self):
        print("A protector")

    def use_special_power(self):
        return f'Using some protection'