""" excerpts taken from https://github.com/scipython/scipython-maths/blob/
master/maze/df_maze.py"""

from room import Room
import random


class Dungeon:

    def __init__(self, nx, ny, ix=0, iy=0):
        """initialize dungeon 2D matrix at (0,0)"""
        self.__nx = nx
        self.__ny = ny
        self.__ix = ix
        self.__iy = iy
        self.__current_room = 0, 0
        self.__maze = [[Room(x, y) for y in range(ny)] for x in range(nx)]
        self.__entrance_room = 0, 0         # Dee: keep location of the entrance
        self.__exit_room = 0, 0             # Dee: keep location of the exit
        self.__pillar_a = 0, 0              # Dee: keep location of the pillar A
        self.__pillar_e = 0, 0              # Dee: keep location of the pillar E
        self.__pillar_i = 0, 0              # Dee: keep location of the pillar I
        self.__pillar_p = 0, 0              # Dee: keep location of the pillar P

        self.count = 0

    def room_at(self, x, y):
        """Return the Room at (x,y)"""
        return self.__maze[x][y]

    def get_nx(self):
        return self.__nx

    def get_ny(self):
        return self.__ny

    def find_neighbors(self, room):
        """Return a list of unvisited neighbors to room."""
        # options to go to find neighbors
        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbors = []
        for direction, (dx, dy) in delta:
            x2, y2 = room.x + dx, room.y + dy
            if (0 <= x2 < self.__nx) and (0 <= y2 < self.__ny):
                neighbour = self.room_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbors.append((direction, neighbour))
        return neighbors

    def make_dungeon(self):
        # Total number of rooms
        n = self.__nx * self.__ny
        room_stack = []
        current_room = self.room_at(self.__ix, self.__iy)
        # Total number of visited rooms during maze construction
        nv = 1

        # iterate over all rooms of dungeon
        while nv < n:
            neighbors = self.find_neighbors(current_room)

            if not neighbors:
                # We've reached a dead end: backtrack.
                current_room = room_stack.pop()
                continue

            # Choose a random neighboring room and move to it
            direction, next_room = random.choice(neighbors)
            current_room.connect(next_room, direction)
            room_stack.append(current_room)
            current_room = next_room
            nv += 1

    def place_dungeon_items(self):
        self.place_entrance()
        self.place_exit()
        self.place_pillar_a()
        self.place_pillar_e()
        self.place_pillar_i()
        self.place_pillar_p()
        self.place_pits()
        self.place_vision()
        self.place_healing()

    def place_entrance(self):
        x = self.__ix
        y = self.__iy
        self.__current_room = x, y
        self.__entrance_room = x, y
        self.__maze[x][y].set_entrance(True)

    def current_room(self):
        return self.__current_room

    # Dee: return location of the entrance
    def entrance_room(self):
        return self.__entrance_room

    # Dee: return location of the exit
    def exit_room(self):
        return self.__exit_room

    # Dee: return location of the pillar A room
    def pillar_a_room(self):
        return self.__pillar_a

    # Dee: return location of the pillar E room
    def pillar_e_room(self):
        return self.__pillar_e

    # Dee: return location of the pillar I room
    def pillar_i_room(self):
        return self.__pillar_i

    # Dee: return location of the pillar P room
    def pillar_p_room(self):
        return self.__pillar_p

    def move_to(self, x, y):
        self.__current_room = x, y

    def place_exit(self):
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__exit_room = x, y
        self.__maze[x][y].set_exit(True)

    def place_pillar_a(self):
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__pillar_a = x, y
        self.__maze[x][y].set_pillar_a(True)

    def place_pillar_e(self):
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__pillar_e = x, y
        self.__maze[x][y].set_pillar_e(True)

    def place_pillar_i(self):
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__pillar_i = x, y
        self.__maze[x][y].set_pillar_i(True)

    def place_pillar_p(self):
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__pillar_p = x, y
        self.__maze[x][y].set_pillar_p(True)

    def place_pits(self, probability=.1):
        num_pits = (self.__nx * self.__ny) * probability  # probability of having a pit
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__maze[x][y].set_pit(True)

    def place_healing(self):
        num_healing = (self.__nx * self.__ny) * .1  # 10% probability of having a healing potion
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__maze[x][y].set_healing_potion(True)

    def place_vision(self):
        num_vision = (self.__nx * self.__ny) * .1  # 10% probability of having vision potion
        x = random.randint(0, (self.__nx - 1))
        y = random.randint(0, (self.__ny - 1))
        self.__maze[x][y].set_vision_potion(True)

    def __repr__(self):
        """Return a string representation of the maze."""

        # A: creates northern border of dungeon
        dungeon_rows = ['*' * (self.__nx * 2 + 1)]
        # B: creates a maze row for ny (except the last row)
        for y in range(self.__ny - 1):
            maze_row = ['*']
            # creates a wall if wall to the east is true (excludes last column)
            for x in range(self.__nx - 1):
                maze_row.append(self.__maze[x][y].get_letter())
                if self.__maze[x][y].walls['E']:
                    maze_row.append('|')
                else:
                    maze_row.append(' ')
            # creates eastern border of dungeon
            maze_row.append(self.__maze[x+1][y].get_letter())
            maze_row.append('*')
            dungeon_rows.append(''.join(maze_row))
            # C: adds rows of walls between rooms if S wall is True
            maze_row = ['*']
            for x in range(self.__nx):
                # creates a wall if wall to the east is true
                if self.__maze[x][y].walls['S']:
                    maze_row.append('-*')
                else:
                    maze_row.append(' *')

            dungeon_rows.append(''.join(maze_row))

        # append last room of the maze
        for y in range(self.__ny - 1, self.__ny):
            maze_row = ['*']
            # creates a wall if wall to the east is true (excludes last column)
            for x in range(self.__nx - 1):
                maze_row.append(self.__maze[x][y].get_letter())
                if self.__maze[x][y].walls['E']:
                    maze_row.append('|')
                else:
                    maze_row.append(' ')
            # creates eastern border of dungeon
            maze_row.append(self.__maze[x+1][y].get_letter())
            maze_row.append('*')
            dungeon_rows.append(''.join(maze_row))
            # C: adds rows of walls between rooms if S wall is True
            maze_row = ['*']
            maze_row.append('**' * self.__nx)
            dungeon_rows.append(''.join(maze_row))

        return '\n'.join(dungeon_rows)

    def print_maze_contents(self):
        for row in range(0, self.__ny):
            print("row ", row)
            for col in range(0, self.__nx):
                print(self.__maze[row][col].__str__())
            print()

    def count_pillars_and_exit(self, row, col):
        # first find Pillar A, then reset visited, then find Pillar E, then reset
        # visited, then

        if not self.is_valid_room(row, col) or self.__maze[row][col].is_visited():
            return 0

        # check for exit or any pillar
        item_count = 0
        if self.__maze[row][col].is_exit():
            item_count = 1
        elif self.__maze[row][col].is_pillar_a():
            item_count = 1
        elif self.__maze[row][col].is_pillar_e():
            item_count = 1
        elif self.__maze[row][col].is_pillar_i():
            item_count = 1
        elif self.__maze[row][col].is_pillar_p():
            item_count = 1

        # not at exit so try another room: south, east, north, west
        self.__maze[row][col].set_visited(True)
        # if east_wall is not true, then we can go row +1
        if self.__maze[row][col].walls['E'] is False:
            item_count += self.count_pillars_and_exit(row + 1, col)
        if self.__maze[row][col].walls['S'] is False:
            item_count += self.count_pillars_and_exit(row, col + 1)
        if self.__maze[row][col].walls['W'] is False:
            item_count += self.count_pillars_and_exit(row - 1, col)
        if self.__maze[row][col].walls['N'] is False:
            item_count += self.count_pillars_and_exit(row, col - 1)

        return item_count

    def traverse(self):
        return self.count_pillars_and_exit(0, 0) == 5

    def is_valid_room(self, row, col):
        return 0 <= row < self.__nx and 0 <= col < self.__ny and self.__maze[row][col].can_enter()



maze1 = Dungeon(5, 5, 0, 0)
print("initial matrix")
print(maze1)
maze1.make_dungeon()
print("\n\ncreate maze")
print(maze1)
print("\n\nPlace Items")
maze1.place_entrance()
maze1.place_exit()
maze1.place_pillar_a()
maze1.place_pillar_e()
maze1.place_pillar_i()
maze1.place_pillar_p()
# maze1.place_pits()
# maze1.place_vision()
# maze1.place_healing()


print(maze1)
print("Traverse: ", maze1.traverse())
print("Entrance: " + str(maze1.entrance_room()))
print("Exit: " + str(maze1.exit_room()))
print("Pillar A: " + str(maze1.pillar_a_room()))

# res = maze1.can_travers_to_pillar_a()
# print(res)
# res = maze1.can_travers_to_pillar_e()
# print(res)
# res = maze1.can_travers_to_pillar_i()
# print(res)
# res = maze1.can_travers_to_pillar_p()
# print(res)
# res = maze1.can_travers_to_exit()
# print(res)