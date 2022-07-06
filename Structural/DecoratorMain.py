
from Structural.Decorator.Fighter import Fighter
from Structural.Decorator.Tank import Protector
from Structural.Decorator.Sword import Sword
from Structural.Decorator.Shield import Shield

if __name__ == "__main__":

    boyka = Fighter()
    mastin = Protector()
    print("--- Without decorator ---")
    print("Boyka")
    print(boyka.fight())
    print()
    print("Mastin")
    print(mastin.defend())
    print()
    print("--- Using the decorator ---")
    print("Boyka")
    boyka = Sword(boyka)
    print(boyka.use_special_power())
    print()
    print("Mastin")
    mastin = Shield(mastin)
    print(mastin.use_special_power())



