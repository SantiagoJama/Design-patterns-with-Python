from Creational.FactoryMethod.FactoryMethodV1 import Factory
from Creational.FactoryMethod.FactoryMethodV2 import FurnitureFactory

if __name__ == "__main__":
    print("==================== FACTORY METHOD V1 ==============")

    my_product_from_factory = Factory()
    # Circle
    print("**** CIRCLE ****")
    my_circle_shape = my_product_from_factory.create_figure('Circle')
    my_circle_shape.rotate_in_grade(100)

    # Rectangle
    print("**** RECTANGLE ****")
    my_rectangle_shape = my_product_from_factory.create_figure('rectangle')
    my_rectangle_shape.rotate_in_grade(300)

    # Square
    print("**** SQUARE ****")
    my_square_shape = my_product_from_factory.create_figure('square')
    my_square_shape.rotate_in_grade(180)
    print()
    print()


    print("================== FACTORY METHOD V2 =====================")
    print("----- Furniture Factory -----")

    furniture_factory = FurnitureFactory()
    print("***** PLASTIC CHAIR *****")
    plastic_chair_furniture = furniture_factory.create_my_furniture('chair')
    plastic_chair_furniture.create_furniture('plastic')
    print()
    print("***** WOOD CHAIR *****")
    wood_table_furniture = furniture_factory.create_my_furniture('chair')
    wood_table_furniture.create_furniture('wood')
    print()

    print("**** PLASTIC TABLE ****")
    plastic_table_furniture = furniture_factory.create_my_furniture('table')
    plastic_table_furniture.create_furniture('plastic')
    print()
    print("***** WOOD TABLE *****")
    wood_table_furniture = furniture_factory.create_my_furniture('table')
    wood_table_furniture.create_furniture('wood')
    print()

    print("**** PLASTIC SHELVE ****")
    plastic_shelve_furniture = furniture_factory.create_my_furniture('shelve')
    plastic_shelve_furniture.create_furniture('plastic')
    print()
    print("***** WOOD SHELVE *****")
    wood_shelve_furniture = furniture_factory.create_my_furniture('shelve')
    wood_shelve_furniture.create_furniture('wood')
    print()
    print()
