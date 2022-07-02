from Structural.Adapter import Birds
from Structural.Adapter.Person import Person


class FlyAdapter(Birds.Birds):

    def __init__(self):
        self.person = Person()

    def run(self):
        self.person.run()

    def fly(self):
        self.person.fly_with_jetpack()
