class SingletonCoreV1(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            new_instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = new_instance
        return cls.__instances[cls]

    @staticmethod
    def get_all_instance():
        print(SingletonCoreV1.__instances)


class SingletonV1(metaclass=SingletonCoreV1):
    def some(self):
        pass


class SingletonCoreV2:
    __singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.__singleton:
            cls.__singleton = super(SingletonCoreV2, cls).__new__(cls, *args, **kwargs)
        return cls.__singleton


    def get_all_instances():
        print(SingletonCoreV2.__singleton)
