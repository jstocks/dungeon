import random


class Adventurer:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(75, 100)
        self.healing_potions = 0
        self.vision_potions = 0
        # must decide if pillars should be number, list, dictionary, or separate.
        # separate pillars:
        self.pillars = {"A": False, "E": False, "I": False, "P": False}

    def consume_healing_potion(self):
        if self.healing_potions > 0:
            self.change_hp(25)  # Must decide how much health healing potion recovers
            self.healing_potions -= 1

    def change_hp(self, amount):
        if amount < 0:
            self.hp -= amount
        else:
            self.hp += amount
            if self.hp > 100:  # Do we want max hp to be 100?
                self.hp = 100

    def all_pillars_found(self):
        pillars = 0
        for value in self.pillars.values():
            if value:
                pillars += 1
        if pillars == 4:
            return True
        else:
            return False

    def __str__(self):
        return "{self.name}:\n" \
               "HP: {self.hp}\n" \
               "Healing Potions: {self.healing_potions}\n" \
               "Vision Potions: {self.vision_potions}\n" \
               "Pillars found: {self.pillars}".format(self=self)


if __name__ == '__main__':
    kishan = Adventurer("John")
    print(kishan)
    kishan.pillars["A"] = True
    print(kishan)
    print(kishan.all_pillars_found())
    kishan.pillars["E"] = True
    kishan.pillars["I"] = True
    kishan.pillars["P"] = True
    print(kishan.all_pillars_found())



