from Singleton import SingletonV1, SingletonCoreV2
from FactoryMethodV1 import Factory
from FactoryMethodV2 import FurnitureFactory

if __name__ == "__main__":
    print("================== SINGLETON ===================")
    obj1 = SingletonV1()
    obj2 = SingletonV1()

    if id(obj1) == id(obj2):
        print("Both contain the same object ")
    else:
        print("Error in the implementation")

    print(obj1)
    print(obj2)
    SingletonV1.get_all_instance()
    print(type(SingletonV1.get_all_instance()))

    print("****** USING SINGLETON V2 ********")
    ob1 = SingletonCoreV2()
    ob2 = SingletonCoreV2()

    print(ob1)
    print(ob2)
    SingletonCoreV2.get_all_instances()



    print()
    print("==================== FACTORY METHOD ==============")

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

    print("================== FACTORY METHOD =====================")
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



