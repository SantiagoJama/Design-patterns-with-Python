class SingletonCore(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            new_instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = new_instance
        return cls.__instances[cls]

    @staticmethod
    def all_instance():
        print(SingletonCore.__instances)


class Singleton(metaclass=SingletonCore):

    def some(self):
        pass
