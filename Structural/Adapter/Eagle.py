from Structural.Adapter import Birds


class Eagle(Birds.Birds):

    def run(self):
        print("The eagle is running")

    def fly(self):
        print("The eagle is flying")
