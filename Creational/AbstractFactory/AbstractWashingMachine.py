from abc import ABC, abstractmethod


class AbstractWashingMachine(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_washing_program(self):
        pass
