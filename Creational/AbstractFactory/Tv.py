from Creational.AbstractFactory.AbstractTv import AbstractTv


class LcdTv(AbstractTv):

    def __init__(self):
        print("LCD TV Constructor")

    def turn_on(self):
        print("LCD Tv is on")

    def turn_off(self):
        print("LCD Tv is off")

    def change_channel_up(self):
        print("LCD Tv change changed to a higher channel")

    def change_channel_down(self):
        print("LCD Tv change changed to a lower channel")

    def decrease_volume(self):
        print("LDC TV Turned up volume")

    def raise_volume(self):
        print("LCD TV Turned down volume")


class PlasmaTv(AbstractTv):

    def __init__(self):
        print("PLASMA TV Constructor")

    def turn_on(self):
        print("PLASMA Tv is on")

    def turn_off(self):
        print("PLASMA Tv is off")

    def change_channel_up(self):
        print("PLASMA Tv change changed to a higher channel")

    def change_channel_down(self):
        print("PLASMA Tv change changed to a lower channel")

    def decrease_volume(self):
        print("PLASMA TV Turned up volume")

    def raise_volume(self):
        print("PLASMA TV Turned down volume")


class LedTv(AbstractTv):

    def __init__(self):
        print("LED TV Constructor")

    def turn_on(self):
        print("LED Tv is on")

    def turn_off(self):
        print("LED Tv is off")

    def change_channel_up(self):
        print("LED Tv change changed to a higher channel")

    def change_channel_down(self):
        print("LED Tv change changed to a lower channel")

    def decrease_volume(self):
        print("LED TV Turned up volume")

    def raise_volume(self):
        print("LED TV Turned down volume")