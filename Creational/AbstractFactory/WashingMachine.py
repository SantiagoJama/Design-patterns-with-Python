from Creational.AbstractFactory.AbstractWashingMachine import AbstractWashingMachine


class BigWashingMachine(AbstractWashingMachine):

    def __init__(self):
        print("Big Washing Machine constructor")

    def turn_on(self):
        print("The big washing machine is on")

    def turn_off(self):
        print("The big washing machine is off")

    def set_washing_program(self):
        print("Washing program for big washing machine is ready")


class MediumWashingMachine(AbstractWashingMachine):

    def __init__(self):
        print("Medium Washing Machine constructor")

    def turn_on(self):
        print("Medium washing machine is on")

    def turn_off(self):
        print("Medium washing machine is off")

    def set_washing_program(self):
        print("Washing program for Medium washing machine is ready")


class SmallWashingMachine(AbstractWashingMachine):

    def __init__(self):
        print("Small Washing Machine constructor")

    def turn_on(self):
        print("Small big washing machine is on")

    def turn_off(self):
        print("Small big washing machine is off")

    def set_washing_program(self):
        print("Washing program for Small washing machine is ready")
