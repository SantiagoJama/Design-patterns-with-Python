from abc import abstractmethod, ABC


class Furniture(ABC):

    @abstractmethod
    def create_furniture(self, material):
        pass


class Chair(Furniture):

    def __init__(self):
        print("Chair constructor")

    def create_furniture(self, material):
        if material.lower() == 'plastic':
            print("Factory created a Plastic Chair")
        elif material.lower() == 'wood':
            print("Factory created a Wood Chair")
        else:
            print("what material?")


class Table(Furniture):

    def __init__(self):
        print("Table constructor")

    def create_furniture(self, material):
        if material.lower() == 'plastic':
            print("Factory created a Plastic Table")
        elif material.lower() == 'wood':
            print("Factory created a Wood Table")
        else:
            print("what material?")


class Shelve(Furniture):

    def __init__(self):
        print("Shelve constructor")

    def create_furniture(self, material):
        if material.lower() == 'plastic':
            print("Factory created a Plastic Shelve")
        elif material.lower() == 'wood':
            print("Factory created a Wood Shelve")
        else:
            print("what material?")


class FurnitureFactory:

    def __init__(self):
        print("Furniture factory constructor")

    def create_my_furniture(self, furniture_type):
        if furniture_type.lower() == 'chair':
            return Chair()
        elif furniture_type.lower() == 'table':
            return Table()

        elif furniture_type.lower() == 'shelve':
            return Shelve()

        else:
            return None

