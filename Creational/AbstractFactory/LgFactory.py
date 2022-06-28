from Creational.AbstractFactory.AbstractFactory import AbstractFactory
from Creational.AbstractFactory.Tv import PlasmaTv, LcdTv, LedTv
from Creational.AbstractFactory.WashingMachine import BigWashingMachine, MediumWashingMachine, SmallWashingMachine


class LgFactory(AbstractFactory):

    def create_tv(self, tv_type):
        if tv_type.lower() == 'plasma':
            return PlasmaTv()
        elif tv_type.lower() == 'lcd':
            return LcdTv
        elif tv_type.lower() == 'led':
            return LedTv()
        else:
            return None

    def create_washing_machine(self, machine_type):
        if machine_type.lower() == 'big':
            return BigWashingMachine()
        elif machine_type.lower() == 'medium':
            return MediumWashingMachine()
        elif machine_type.lower() == 'small':
            return SmallWashingMachine()
        else:
            return None
