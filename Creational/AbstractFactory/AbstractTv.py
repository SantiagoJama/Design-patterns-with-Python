from abc import ABC, abstractmethod


class AbstractTv(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def change_channel_up(self):
        pass

    @abstractmethod
    def change_channel_down(self):
        pass

    @abstractmethod
    def decrease_volume(self):
        pass

    @abstractmethod
    def raise_volume(self):
        pass
