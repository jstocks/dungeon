from adventurer import Adventurer
from dungeon import Dungeon
from room import Room


"""DungeonAdventure holds the logic of playing the game.  Re/starts game, creates
adventurer and dungeon through respective classes, controls user input/options,
and logic for winning game"""


def start_game():
    """This method starts the game.  Provides an introduction and how to play guide.
    It also kicks off the game with character name and difficulty."""
    intro()
    how_to_play()
    adventurer = create_adv()
    dungeon = difficulty()
    play(dungeon, adventurer)


def restart_game():
    """This method restarts the game without intro / how to play guide."""
    adventurer = create_adv()
    dungeon = difficulty()
    play(dungeon, adventurer)


def play(dungeon, adventurer):
    """This method holds the logic for playing the game."""
    print_room(dungeon)
    user_input(dungeon, adventurer)
    hidden_menu()
    # print_dungeon()
    game_over()


def intro():
    """This method provides an overview of the game"""
    print("Welcome to the Dungeon of Doom!  Prepare for the most difficult \n"
          "challenge of your adventure-seeking life.  Check your pride at the door,\n"
          "and bring an extra ounce of courage as you face off against countless\n"
          "pits and race against your own agony to capture the elusive....... \n\n"
          "*****  Four Pillars of Object-Oriented Programming *****\n")


def how_to_play():
    """This method describes the goal of the game, how to win, and the objects
    encountered during the game"""
    print("The goal of this game is to escape the dungeon maze after finding the\n"
          "four pillars:\n"
          "   1: Abstraction\n"
          "   2: Encapsulation\n"
          "   3: Inheritance\n"
          "   4: Polymorphism\n\n"

          "Be warned - you have limited health points [HP]. If you fall in a pit, you\n"
          "will lose HP. Don't fret - there are also Healing Potions and Vision\n"
          "Potions scattered about the dungeon to help you in your quest. Once you\n"
          "collect all Four Pillars of OO, the exit door will unlock --- if you reach\n"
          "the exit before your HP reaches a big fat zero, you win!\n\n"
          "Move throughout the map by typing \'u\', \'d\', \'l\', or \'r\'\n"
          "You can only move through the doors that exist in the dungeon.\n\n"
          "Check the status of your adventurer by typing \'s\'.\n\n"
          "Be strong in your journey...\n\"Even death is not to be feared by one who "
          "has lived wisely\" --- Buddha\n")


def create_adv():
    """This method asks user for Character Name input. This should reference the
    Adventurer Class"""
    player_name = input("Welcome to the bridge of death... What is your name?: ")
    return Adventurer(player_name)


def difficulty():
    """This method will define the size of the dungeon array.  1 = 3x3, 2 = 5x5, 3 = 6x6"""
    low = 1
    high = 5
    level = int(input("What is your quest? Enter a difficulty from 1 (Easy) to 5 (Hard): "))
    if low <= level <= high:
        # create dungeon by array size based on level input
        if level == 1:
            nx, ny = 5, 5
        if level == 2:
            nx, ny = 6, 6
        if level == 3:
            nx, ny = 7, 7
        if level == 4:
            nx, ny = 8, 8
        if level == 5:
            nx, ny = 10, 10
        ix, iy = 0, 0
        game_board = Dungeon(nx, ny, ix, iy)
        game_board.make_dungeon()
        game_board.place_dungeon_items()
        while game_board.traverse() is not True:
            game_board.make_dungeon()
            game_board.place_dungeon_items()
        print(game_board)
        return game_board
    else:
        print("\n\"Ahhhhhhhhhhhhh\" (That's the sound of you being thrown into "
              "the gorge because you didn't enter an integer between 1-5.)  Game over.\n")
        input("Press Enter to restart game...")
        restart_game()


def print_room(dungeon):
    # visualize the room here
    x, y = dungeon.current_room()
    room = dungeon.room_at(x, y)

    print("*", end='')
    if y == 0:
        print("*", end='')
    else:  # it's not border
        if room.has_north_wall():
            print("-", end='')
        else:
            print(" ", end='')
    print("*")

    if x == 0:
        print("*", end='')
    else:  # it's not border
        if room.has_west_wall():
            print("|", end='')
        else:
            print(" ", end='')

    print(room.get_letter(), end='')

    if x == dungeon.get_nx():
        print("*", end='')
    else:  # it's not border
        if room.has_east_wall():
            print("|", end='')
        else:
            print(" ", end='')

    print("")
    print("*", end='')
    if y == dungeon.get_ny():
        print("*", end='')
    else:
        if room.has_south_wall():
            print("-", end='')
        else:
            print(" ", end='')
    print("*")

def use_vision_potion(dungeon):
    x, y = dungeon.current_room()
    room = dungeon.room_at(x, y)

    pass


def user_input(dungeon, adventurer):
    """This method will allow the user to perform a set of tasks based on the room and
    inventory the adventurer holds:  Move, use healing/vision potion, view inventory, give up"""
    keystroke = input("What would you like to do? Press \"1\" for all options: ")
    # print all options

    player = adventurer
    x, y = dungeon.current_room()
    room = dungeon.room_at(x, y)
    if keystroke == "1":
        options = []
        if dungeon.is_valid_room(x, y) is True and room.has_north_wall() is False:
            options.append("u")
        if dungeon.is_valid_room(x, y) is True and room.has_south_wall() is False:
            options.append("d")
        if dungeon.is_valid_room(x, y) is True and room.has_east_wall() is False:
            options.append("r")
        if dungeon.is_valid_room(x, y) is True and room.has_west_wall() is False:
            options.append("l")
        # if adventurer.has_healing_potion is > 0:
        #     options.append("h")
        # if adventurer.has_vision_potion is True:
        #     options.append("v")
        # View Status
        options.append("s")
        options.append("q")
        print(options)
        print_room(dungeon)
        user_input(dungeon, adventurer)

    # quit option
    elif keystroke == "q":
        a = input("Temptation to quit is the greatest just before you are about "
                  "to succeed.\nDo you really want to give up? (y or n): ")
        if a == "y":
            print("\nThere is a difference between giving up and knowing when you had enough.\n\n"
                  "Better luck next time.  Game over.\n")
            input("Press Enter to restart or exit the game.")
            restart_game()
        elif a == "n":
            print_room(dungeon)
            user_input(dungeon, adventurer)
        else:
            print("That is not a valid command. Try again.")
    # move adventurer
    elif keystroke == "u":
        # need to validate if it is possible to move up
        # if it is not possible then use the keyword break
        x, y = dungeon.current_room()
        if dungeon.is_valid_room(x, y) is True and room.has_north_wall() is False:
            dungeon.move_to(x, y - 1)
        else:
            print("That is not a valid command.  Try again. ")
    elif keystroke == "d":
        x, y = dungeon.current_room()
        if dungeon.is_valid_room(x, y) is True and room.has_south_wall() is False:
            dungeon.move_to(x, y + 1)
        else:
            print("That is not a valid command.  Try again. ")
    elif keystroke == "l":
        x, y = dungeon.current_room()
        if dungeon.is_valid_room(x, y) is True and room.has_west_wall() is False:
            dungeon.move_to(x - 1, y)
        else:
            print("That is not a valid command.  Try again. ")
    elif keystroke == "r":
        x, y = dungeon.current_room()
        if dungeon.is_valid_room(x, y) is True and room.has_east_wall() is False:
            dungeon.move_to(x + 1, y)
        else:
            print("That is not a valid command.  Try again. ")

    elif keystroke == "s":
        print("Status:")
        print(player)
        print_room(dungeon)
        user_input(dungeon, adventurer)
    # use healing potion
    # elif keystroke == "h":
    #     adventurer.use_healing_potion():
    #
    # # use vision potion
    # elif keystroke == "v":
    #     if adventurer.has_vision_potion():

    # hidden menu item to show map
    elif keystroke == "map":
        print(dungeon)
    else:
        print("That is not a valid command.  Try again. ")
        print_room(dungeon)
    # prints new room, then prompts for next user input

    # discover_room() # will pick up potion, discover pillar, or hurt you via pit
    # check for pick_up healing potion if....
    # check for pick up vision if...
    # check for pit, hurt if so...

    print_room(dungeon)
    user_input(dungeon, adventurer)


def hidden_menu():
    """This method provides a hidden menu feature that prints out the entire dungeon
    for testing / easter egg purposes"""
    # currently built into the user_input method "map"
    pass


def print_dungeon():
    """This method prints the entire dungeon; to be used in hidden menu or at end of game"""
    pass


def game_over(dungeon):
    """This method determines the end of the game --- 1) LOSE if hero runs out of HP
     2) WIN if the adventurer collects all four pillars and finds the exit."""
    if Adventurer.is_alive is False:
        print("It is not just a flesh wound this time.  You died.")
        print(dungeon)
        roll_credits()
        input("Press Enter to restart game...")
        restart_game()
    if Adventurer.all_pillars_found:
        if Room.is_exit:
            print("Horace Mann once said, \"Be ashamed to die until you have "
                  "won some victory for humanity.\"  And today, you won!\n\n"
                  "Congratulations!  You defeated the Dungeon of Doom!\n\n")
            print(dungeon)
            roll_credits()

def roll_credits():
    print("Created by Dee \"Python Slayer\" Turco, Kishan \"Code Killer\" Vekaria, "
          "and Jeff \"Algo Assassin\" Stockman")


start_game()