<<<<<<< HEAD
class Room:
    def __init__(self):
        self.__healing_portion = False
        self.__pit = False
        self.__pillar = "No pillar"
        self.__vision = False
        self.__exit = False
        self.__entrance = False
        self.__impassable = False
        self.__visited = False
        self.__item_count = 0

    def get_healing_portion(self):
        return self.__healing_portion

    def set_healing_portion(self):
        self.__healing_portion = True
        self.__item_count += 1

    def get_pit(self):
        return self.__pit

    def set_pit(self):
        self.__pit = True

    def get_pillar(self):
        return self.__pillar

    def set_pillar(self):
        self.__pillar = True
        self.__item_count += 1

    def get_vision(self):
        return self.__vision

    def set_vision(self):
        self.__vision = True
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

    def has_been_visited(self):
        return self.__visited is True

    def is_multiple_item(self):
        return self.__item_count > 1

    def __str__(self):
        return "Healing Portion: " + str(self.__healing_portion) + "\n" \
            + "Pit: " + str(self.__pit) + "\n" \
            + "Pillar: " + str(self.__pillar) + "\n" \
            + "Vision: " + str(self.__pillar) + "\n" \
            + "Exit: " + str(self.__exit) + "\n" \
            + "Entrance: " + str(self.__entrance) + "\n" \
            + "Impassable: " + str(self.__impassable) + "\n" \
            + "Visited: " + str(self.__visited)

=======
from door import Door


class Room:
    def __init__(self, *args, **kwargs):
        for arg in args:
            if arg == "H":
                self.__has_healing_portion = True
            if arg == "X":
                self.__has_pit = True
            if arg == "A":
                self.__has_pillar_A = True
            if arg == "E":
                self.__has_pillar_E = True
            if arg == "I":
                self.__has_pillar_I = True
            if arg == "P":
                self.__has_pillar_P = True
            if arg == "V":
                self.__has_vision = True
            if arg == "O":
                self.__exit = True
            if arg == "i":
                self.__entrance = True
            if arg == "":
                self.__space = True
            if arg == "M":
                self.__has_healing_portion = True
                self.__has_pillar = True
                self.__has_vision = True

        for key, value in kwargs.items():
            if key == "front":
                self.__font_door = Door(value)
            if key == "back":
                self.__back_door = Door(value)
            if key == "top":
                self.__top_door = Door(value)
            if key == "bottom":
                self.__bottom_door = Door(value)

    def has_healing_portion(self):
        return self.__has_healing_portion is True

    def has_pit(self):
        return self.__has_pit is True

    def has_pillar_a(self):
        return self.__has_pillar_A is True

    def has_pillar_e(self):
        return self.__has_pillar_E is True

    def has_pillar_i(self):
        return self.__has_pillar_I is True

    def has_pillar_p(self):
        return self.__has_pillar_P is True

    def has_vision(self):
        return self.__has_vision is True

    def is_room_empty(self):
        return self.__space is True

    def has_entrance(self):
        return self.__entrance is True

    def has_exit(self):
        return self.__exit is True

    def open_front_door(self):
        return self.__font_door.is_lock() is True

    def open_back_door(self):
        return self.__back_door.is_lock() is True

    def open_top_door(self):
        return self.__top_door.is_lock() is True

    def open_bottom_door(self):
        return self.__bottom_door.is_lock() is True


inside = {"H", "V", "i"}
door = {'font': True, 'back': False, 'top': False, 'bottom': False}
rm = Room(inside, door)

rm.has_pit()
>>>>>>> 14eef56 (Add files via upload)





