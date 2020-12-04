
class Door:
    def __init__(self, lock=True):
        self.__lock = lock

    def is_lock(self):
        return self.__lock is True


