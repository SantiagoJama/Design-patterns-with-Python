from Creational.AbstractFactory.LgFactory import LgFactory
from Creational.AbstractFactory.SamsungFactory import SamsungFactory


class FactoryProvider:

    def __init__(self):
        print("Factory Provider constructor")

    def select_factory_for_your_product(self, factory):
        if factory.lower() == 'samsung':
            return SamsungFactory()
        else:
            return LgFactory()
