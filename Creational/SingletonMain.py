from Creational.Singleton.Singleton import SingletonV1, SingletonCoreV2


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







