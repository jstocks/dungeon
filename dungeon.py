from room import Room


class Dungeon:

    def __init__(self, row_count, col_count):
        self.__maze = []
        self.__rowCount = row_count
        self.__colCount = col_count

        for r in range(0, self.__rowCount):
            self.__maze.append([Room() for c in range(0, self.__colCount)])

    def print_maze(self):
        # print(self.__maze)
        for row in range(0, self.__rowCount):
            print("row ", row)
            for col in range(0, self.__colCount):
                print(self.__maze[row][col].__str__())
            print()

    def set_health_potion(self, row, col):
        self.__maze[row][col].set_health(True)

    # WARNING: Work in progress ;-)
    def traverse(self, row, col):
        found_exit = False
        if self.is_valid_room(row, col):
            # check for exit
            if self.__maze[row][col].is_exit():
                return True
            # not at exit so try another room: south, east, north, west
            found_exit = self.traverse(row + 1, col)
            if not found_exit:
                found_exit = self.traverse(row, col + 1)
            if not found_exit:
                found_exit = self.traverse(row - 1, col)
            if not found_exit:
                found_exit = self.traverse(row, col - 1)

            # if we did not reach the exit from this room we need mark it as visited to
            # avoid going into the room again
            if not found_exit:
                self.__maze[row][col].set_visited(True)

        else:  # tried to move into a room that is not valid
            return False
        return found_exit

    def is_valid_room(self, row, col):
        return 0 <= row < self.__rowCount and 0 <= col < self.__colCount and self.__maze[row][col].can_enter()

    def adventurer_location(self):
        pass

dungeon = Dungeon(2, 4)
dungeon.set_health_potion(0, 0)
dungeon.print_maze()
