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
        self.alive = True

    def pick_up_healing_potion(self):
        self.healing_potions += 1
        print("Found a Healing Potion!")

    def pick_up_vision_potion(self):
        self.vision_potions += 1
        print("Found a Vision Potion!")

    def pick_up_pillar(self, pillar):
        if pillar == "A" or \
                pillar == "E" or \
                pillar == "I" or \
                pillar == "P":
            self.pillars[str(pillar).upper()] = True
            print("You found pillar " + str(pillar).upper() + "!")
        else:
            raise ValueError("A pillar must be A, E, I, or P")

    def use_vision_potion(self):  # Not sure just yet how this will work with room
        print("Used a Vision Potion!")
        pass

    def use_healing_potion(self):
        if self.healing_potions > 0:
            self.change_hp(25)  # Must decide how much health healing potion recovers
            self.healing_potions -= 1
            print("Used a healing potion!\n"
                  "Current HP: " + str(self.hp))
        else:
            print("You don't have any healing potions!")

    def change_hp(self, amount):
        if amount < 0:
            self.hp += amount
        else:
            self.hp += amount
            if self.hp > 100:  # Do we want max hp to be 100?
                self.hp = 100

    def fell_into_pit(self):
        self.change_hp(-25)  # Must determine how much damage a pit does
        if self.hp <= 0:
            self.alive = False
            print("You are dead :(")

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

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

if __name__ == '__main__':
    print("     Creating and printing out the status of a player named John:")
    player = Adventurer("John")
    print(player)
    print("--------------------")
    print("     Picked up pillar 'A', 'E', and 'I'")
    player.pick_up_pillar("A")
    player.pick_up_pillar("E")
    player.pick_up_pillar("I")
    print("     Does player has all 4 pillars?:")
    print(player.all_pillars_found())
    print("     Players picks up the 4th pillar, 'P'")
    player.pick_up_pillar("P")
    print("     Does player has all 4 pillars?:")
    print(player.all_pillars_found())

    print("     Using a healing potion when you don't have any:")
    player.use_healing_potion()
    print("     Picking up a healing potion:")
    player.pick_up_healing_potion()
    print("     Number of healing potions:")
    print(player.healing_potions)
    print("     print player hp:")
    print(player.hp)
    print("     Use healing potion:")
    player.use_healing_potion()
    print("     print player hp:")
    print(player.hp)
    print("     print number of healing potions:")
    print(player.healing_potions)
    print("--------------------")
    print(player)

    print("     \nTAKING DAMAGE UNTIL PLAYER IS DEAD:")
    print("     Fell into pit:")
    player.fell_into_pit()
    print("Current HP:" + str(player.hp))
    print("     Fell into pit:")
    player.fell_into_pit()
    print("Current HP:" + str(player.hp))
    print("     Fell into pit:")
    player.fell_into_pit()
    print("Current HP:" + str(player.hp))
    print("     Fell into pit:")
    player.fell_into_pit()
    print("Current HP:" + str(player.hp))
    print("     Fell into pit:")
    player.fell_into_pit()
    print("Current HP:" + str(player.hp))



