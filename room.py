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





