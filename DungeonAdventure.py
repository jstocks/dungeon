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
    create_adv()
    difficulty()
    play()


def restart_game():
    """This method restarts the game without intro / how to play guide."""
    create_adv()
    difficulty()
    play()


def play():
    """This method holds the logic for playing the game."""
    print_room()
    user_input()
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
          "You can move throughout the map by typing \'u\', \'d\', \'l\', or \'r\'\n"
          "You can only move through the doors that exist in the dungeon.\n\n"
          "Be strong in your journey...\n\"Even death is not to be feared by one who "
          "has lived wisely\" --- Buddha\n")


def create_adv():
    """This method asks user for Character Name input. This should reference the
    Adventurer Class"""
    player_name = input("Welcome to the bridge of death... What is your name? ")
    player = Adventurer(player_name)


def difficulty():
    """This method will define the size of the dungeon array.  1 = 3x3, 2 = 5x5, 3 = 6x6"""
    low = 1
    high = 5
    level = int(input("Welcome, " + Adventurer.get_player_name + ".  What is your"
                      "quest? Enter a difficulty from 1 (Easy) to 5 (Hard): "))
    if low <= level <= high:
        # create dungeon by array size based on level input
        if level == 1:
            game_board = Dungeon(3, 3)
        if level == 2:
            game_board = Dungeon(4, 4)
        if level == 3:
            game_board = Dungeon(6, 6)
        if level == 4:
            game_board = Dungeon(8, 8)
        if level == 5:
            game_board = Dungeon(10, 10)
        # method to create dungeon(game_board)
    else:
        print("\n\"Ahhhhhhhhhhhhh\" (That's the sound of you being thrown into "
              "the gorge because you didn't enter an integer between 1-5.)  Game over.\n")
        input("Press Enter to restart game...")
        restart_game()

    # recursive calls to ensure dungeon is traverable and can find all pillars
    while Dungeon.traverse(game_board) is False or Dungeon.pillarable(game_board) is False:
        # re-create a new game_board
        pass

def print_room():
    #visualize the room here
    pass


def user_input():
    """This method will allow the user to perform a set of tasks based on the room and
    inventory the adventurer holds:  Move, use healing/vision potion, view inventory, give up"""
    keystroke = input("What would you like to do? Press \"1\" for all options.")
    # print all options
    if keystroke == "1":
        options = []
        if Room.move_up is True:
            options.append("u")
        if Room.move_down is True:
            options.append("d")
        if Room.move_left is True:
            options.append("l")
        if Room.move_right is True:
            options.append("r")
        if Adventurer.healing_potions > 0:
            options.append("h")
        if Adventurer.vision_potions > 0:
            options.append("v")
        options.append("q")
        print(options)
        user_input()

    # quit option
    if keystroke == "q":
        a = input("Temptation to quit is the greatest just before you are about "
                  "to succeed.  Do you really want to give up? (y or n) ")
        if a == "y":
            print("There is a difference between giving up and knowing when you had enough.\n"
                  "Better luck next time.  Game over.")
            # press Enter to restart
            restart_game()
        if a == "n":
            user_input()
    # move adventurer
    if keystroke == "u":
        Adventurer.move_up()
    if keystroke == "d":
        Adventurer.move_down()
    if keystroke == "l":
        Adventurer.move_left()
    if keystroke == "r":
        Adventurer.move_right()

    #use healing potion
    if keystroke == "h":
        Adventurer.use_healing_potion()
    # use vision potion
    if keystroke == "v":
        Adventurer.use_vision_potion()

    # hidden menu item to show map
    if keystroke == "map":
        print_dungeon()
    else:
        input("That is not a valid command.  Try again. ")

    # prints new room, then prompts for next user input
    print_room()
    user_input()


def hidden_menu():
    """This method provides a hidden menu feature that prints out the entire dungeon
    for testing / easter egg purposes"""
    # currently built into the user_input method
    pass


def print_dungeon():
    """This method prints the entire dungeon; to be used in hidden menu or at end of game"""
    pass


def game_over():
    """This method determines the end of the game --- 1) LOSE if hero runs out of HP
     2) WIN if the adventurer collects all four pillars and finds the exit."""
    if Adventurer.is_alive is False:
        print("It is not just a flesh wound this time.  You died.")
        Dungeon.print_maze()
        roll_credits()
        input("Press Enter to restart game...")
        restart_game()
    if Adventurer.all_pillars_found:
        if Room.is_exit:
            print("Horace Mann once said, \"Be ashamed to die until you have "
                  "won some victory for humanity.\"  And today, you won!\n\n"
                  "Congratulations!  You defeated the Dungeon of Doom!\n\n")
            roll_credits()

def roll_credits():
    print("Created by Dee \"Python Slayer\" Turco, Kishan \"Code Killer\" Vekaria, "
          "and Jeff \"Algo Assassin\" Stockman")


start_game()