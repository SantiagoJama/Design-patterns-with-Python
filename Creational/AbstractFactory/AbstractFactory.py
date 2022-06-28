from abc import abstractmethod, ABC


class AbstractFactory(ABC):

    @abstractmethod
    def create_tv(self):
        pass

    @abstractmethod
    def create_washing_machine(self):
        pass














