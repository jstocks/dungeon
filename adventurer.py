import random


class Adventurer:
    def __init__(self, name):
        self.__name = name
        self.__health_points = random.randint(75, 100)
        self.__healing_potions = []
        self.__vision_potions = 0
        self.__pillar_a = False
        self.__pillar_e = False
        self.__pillar_i = False
        self.__pillar_p = False
        self.__alive = True

    def get_player_name(self):
        return self.__name

    def is_alive(self):
        return self.__alive

    def pick_up_healing_potion(self):
        healing_potion_amount = random.randint(5, 15)
        self.__healing_potions.append(healing_potion_amount)
        self.__healing_potions.sort()
        print("Found a Healing Potion! It can restore " + str(healing_potion_amount) + " health points.")

    def pick_up_vision_potion(self):
        self.__vision_potions += 1
        print("Found a Vision Potion!")

    def pick_up_pillar(self, pillar):
        if pillar == "A":
            self.__pillar_a = True
        elif pillar == "E":
            self.__pillar_e = True
        elif pillar == "I":
            self.__pillar_i = True
        elif pillar == "P":
            self.__pillar_p = True
            print("You found pillar " + str(pillar).upper() + "!")
        else:
            raise ValueError("A pillar must be A, E, I, or P")

    def use_vision_potion(self):  # Not sure just yet how this will work with room
        print("Used a Vision Potion!")
        pass

    def use_healing_potion(self):
        # make a condition to keep asking user to enter proper input
        condition = False
        # check if player has any potions he can use
        potion_counter = 1
        if len(self.__healing_potions) > 0:
            while not condition:
                # display current health
                print("\nCurrent health: " + str(self.__health_points))
                print("Note: Max Health Points is 100")
                # display the available healing potions player has
                print("Healing potion inventory: ")
                print("Item Number \tPotion strength")
                for potion in self.__healing_potions:
                    print(str(potion_counter) + ": \t \t \t \t" + str(potion))
                    potion_counter += 1
            # while not condition:
                # have player select the potion he wants to use
                potion_to_use = int(input("Select the potion (item number) you would like to use, "
                                          "or enter 0 to cancel: "))
                if potion_to_use == 0:
                    condition = True
                    pass
                # check if input is an available index
                elif 0 < potion_to_use <= len(self.__healing_potions):
                    healing_amount = self.__healing_potions[potion_to_use - 1]
                    self.change_health_points(healing_amount)
                    del self.__healing_potions[potion_to_use - 1]
                    print("You just healed " + str(healing_amount) + " health.\nCurrent health is now " +
                          str(self.__health_points))
                    if self.__health_points == 100:
                        print("You're at full health!")
                    condition = True
                else:
                    print("\nThat's not a proper selection!")

            # self.change_hp(25)  # Must decide how much health healing potion recovers
            # self.healing_potions -= 1
            # print("Used a healing potion!\n"
            #       "Current HP: " + str(self.health_points))
        else:
            print("You don't have any healing potions!")

    def change_health_points(self, amount):
        if amount < 0:
            self.__health_points += amount
        else:
            self.__health_points += amount
            if self.__health_points > 100:  # Do we want max hp to be 100?
                self.__health_points = 100

    def fell_into_pit(self):
        damage = random.randint(-20, -1)
        self.change_health_points(damage)  # Must determine how much damage a pit does
        if self.__health_points <= 0:
            self.__alive = False
            print("You are dead :(")

    def all_pillars_found(self):
        if self.__pillar_a and self.__pillar_e and self.__pillar_i and self.__pillar_p:
            return True
        else:
            return False

    def view_inventory(self):
        print(player)

    def __str__(self):
        return self.__name + ":\n" \
               "HP: " + str(self.__health_points) + "\n" \
               "Healing Potions: " + str(self.__healing_potions) + "\n" \
               "Vision Potions: " + str(self.__vision_potions) + "\n" \
               "Pillars found: \n" \
               "A:\t{}\n" \
               "E:\t{}\n" \
               "I:\t{}\n" \
               "P:\t{}\n".format(self.__pillar_a, self.__pillar_e, self.__pillar_i, self.__pillar_p)


if __name__ == '__main__':
    # print("     Creating and printing out the status of a player named John:")
    player = Adventurer("John")
    # print(player)
    # print("--------------------")
    # print("     Picked up pillar 'A', 'E', and 'I'")
    # player.pick_up_pillar("A")
    # player.pick_up_pillar("E")
    # player.pick_up_pillar("I")
    # print("     Does player has all 4 pillars?:")
    # print(player.all_pillars_found())
    # print("     Players picks up the 4th pillar, 'P'")
    # player.pick_up_pillar("P")
    # print("     Does player has all 4 pillars?:")
    # print(player.all_pillars_found())

    print("     Using a healing potion when you don't have any:")
    player.use_healing_potion()
    print("     Picking up 2 healing potions:")
    player.pick_up_healing_potion()
    player.pick_up_healing_potion()
    print("     Inventory:")
    player.view_inventory()
    print("     Use healing potion:")
    player.use_healing_potion()
    player.view_inventory()
    # print("     print player hp:")
    # print(player.hp)
    # print("     print number of healing potions:")
    # print(player.healing_potions)
    # print("--------------------")
    # print(player)

    # print("     \nTAKING DAMAGE UNTIL PLAYER IS DEAD:")
    # print("     Fell into pit:")
    # player.fell_into_pit()
    # print("Current HP:" + str(player.hp))
    # print("     Fell into pit:")
    # player.fell_into_pit()
    # print("Current HP:" + str(player.hp))
    # print("     Fell into pit:")
    # player.fell_into_pit()
    # print("Current HP:" + str(player.hp))
    # print("     Fell into pit:")
    # player.fell_into_pit()
    # print("Current HP:" + str(player.hp))
    # print("     Fell into pit:")
    # player.fell_into_pit()
    # print("Current HP:" + str(player.hp))
    #
