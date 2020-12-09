import random


class Room:
    def __init__(self):
        self.__healing_potion = False
        self.__pit = False
        self.__pillar_a = False
        self.__pillar_e = False
        self.__pillar_i = False
        self.__pillar_p = False
        self.__vision_potion = False
        self.__exit = False
        self.__entrance = False
        self.__impassable = False
        self.__visited = False
        self.__item_count = 0

    def get_healing_potion(self):
        return self.__healing_potion

    def set_healing_potion(self):
        self.__healing_potion = True
        self.__item_count += 1

    def get_pit(self):
        return self.__pit

    def set_pit(self):
        self.__pit = True
        self.__item_count += 1

    def get_pillar_a(self):
        return self.__pillar_a

    def set_pillar_a(self):
        self.__pillar_a = True
        self.__item_count += 1

    def get_pillar_e(self):
        return self.__pillar_e

    def set_pillar_e(self):
        self.__pillar_e = True
        self.__item_count += 1

    def get_pillar_i(self):
        return self.__pillar_i

    def set_pillar_i(self):
        self.__pillar_i = True
        self.__item_count += 1

    def get_pillar_p(self):
        return self.__pillar_p

    def set_pillar_p(self):
        self.__pillar_p = True
        self.__item_count += 1

    def get_vision_potion(self):
        return self.__vision_potion

    def set_vision_potion(self):
        self.__vision_potion = True
        self.__item_count += 1

    def set_exit(self):
        self.__exit = True

    def is_exit(self):
        return self.__exit

    def set_entrance(self):
        self.__entrance = True

    def set_impassable(self):
        self.__impassable = True

    def can_enter(self):
        return not self.__impassable

    def set_visited(self):
        self.__visited = True

    def reset_visited(self):
        self.__visited = False

    def has_been_visited(self):
        return self.__visited is True

    def is_multiple_item(self):
        return self.__item_count > 1

    def __str__(self):
        return "Healing Portion: " + str(self.__healing_potion) + "\n" \
            + "Pit: " + str(self.__pit) + "\n" \
            + "Pillar: " + str(self.__pillar) + "\n" \
            + "Vision: " + str(self.__vision_potion) + "\n" \
            + "Exit: " + str(self.__exit) + "\n" \
            + "Entrance: " + str(self.__entrance) + "\n" \
            + "Impassable: " + str(self.__impassable) + "\n" \
            + "Visited: " + str(self.__visited)






