from Singleton import Singleton

if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()

    if id(obj1) == id(obj2):
        print("Both contain the same object ")
    else:
        print("Error in the implementation")

    print(obj1)
    print(obj2)
    Singleton.all_instance()
    print(type(Singleton.all_instance()))
