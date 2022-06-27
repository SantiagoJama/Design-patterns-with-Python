from abc import abstractmethod, ABC


class IGeometricFigure(ABC):
    @abstractmethod
    def rotate_in_grade(self, grade):
        pass


""" These classes implement the IGeometricFigure abstract method"""


class Circle(IGeometricFigure):

    def __init__(self):
        print("Circle constructor")

    def rotate_in_grade(self, grade):
        print("The circle figure rotated: {}".format(grade))


class Square(IGeometricFigure):

    def __init__(self):
        print("Square constructor")

    def rotate_in_grade(self, grade):
        print("The square figure rotated: {}".format(grade))


class Rectangle(IGeometricFigure):

    def __init__(self):
        print("Rectangle constructor")

    def rotate_in_grade(self, grade):
        print("The rectangle figure rotated: {}".format(grade))


""" The factory """


class Factory:
    def __init__(self):
        print("Factory constructor...")

    def create_figure(self, figure_type):
        if figure_type is None:
            return None
        elif figure_type.lower() == 'circle':
            return Circle()
        elif figure_type.lower() == 'rectangle':
            return Rectangle()
        elif figure_type.lower() == 'square':
            return Square()
        else:
            return None
