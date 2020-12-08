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
            if key == "up":
                self.__up = Door(value)
            if key == "down":
                self.__down = Door(value)
            if key == "left":
                self.__left = Door(value)
            if key == "right":
                self.__right = Door(value)

    def has_healing_portion(self):
        try:
            return self.__has_healing_portion is True
        except AttributeError:
            print("Room doesn't have Healing Portion")

    def has_pit(self):
        try:
            return self.__has_pit is True
        except AttributeError:
            print("Room doesn't have pit")

    def has_pillar_a(self):
        try:
            return self.__has_pillar_A is True
        except AttributeError:
            print("Room doesn't have pillar A")

    def has_pillar_e(self):
        try:
            return self.__has_pillar_E is True
        except AttributeError:
            print("Room doesn't have pillar E")

    def has_pillar_i(self):
        try:
            return self.__has_pillar_I is True
        except AttributeError:
            print("Room doesn't have pillar I")

    def has_pillar_p(self):
        try:
            return self.__has_pillar_P is True
        except AttributeError:
            print("Room doesn't have pillar P")

    def has_vision(self):
        try:
            return self.__has_vision is True
        except AttributeError:
            print("Room doesn't have vision")

    def is_room_empty(self):
        try:
            return self.__space is True
        except AttributeError:
            print("Room is NOT an empty room")

    def has_entrance(self):
        try:
            return self.__entrance is True
        except AttributeError:
            print("Room has no entrance")

    def has_exit(self):
        try:
            return self.__exit is True
        except AttributeError:
            print("Room has no exit")

    def move_up(self):
        try:
            return self.__up.is_lock() is True
        except AttributeError:
            print("You can't move up")

    def move_down(self):
        try:
            return self.__down.is_lock() is True
        except AttributeError:
            print("You can move down")

    def move_left(self):
        try:
            return self.__left.is_lock() is True
        except AttributeError:
            print("You can't move to the left")

    def move_right(self):
        try:
            return self.__right.is_lock() is True
        except AttributeError:
            print("You can't move to the right")


inside = {"H", "V", "i"}
door = {'up': True, 'down': False, 'left': False, 'right': False}
rm = Room(inside, door)

rm.has_pit()





