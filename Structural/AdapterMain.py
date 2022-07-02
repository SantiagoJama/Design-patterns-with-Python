from Structural.Adapter.Eagle import Eagle
from Structural.Adapter.FlyAdapter import FlyAdapter

if __name__ == "__main__":

    print("============= EAGLE ==============")
    eagle = Eagle()
    eagle.run()
    eagle.fly()

    print("============ FOR PERSON ==========")
    carlos = FlyAdapter()
    carlos.run()
    carlos.fly()

    