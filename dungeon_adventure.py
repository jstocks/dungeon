class DungeonAdventure:
    def __init__(self):
        pass

    """This method starts the game.  Provides an introduction and how to play guide.
    It also kicks off the game with character name and difficulty."""
    def start_game(self):
        DungeonAdventure.intro()
        DungeonAdventure.how_to_play()
        DungeonAdventure.create_adv()
        DungeonAdventure.difficulty()

    """This method restarts the game without intro / how to play guide."""
    def restart_game(self):
        DungeonAdventure.create_adv()
        DungeonAdventure.difficulty()

    """This method provides an overview of the game"""
    def intro(self):
        print("Welcome to the Dungeon of Doom!  Prepare for the most difficult \n"
              "challenge of your adventure-seeking life.  Check your pride at the door,\n"
              "and bring an extra ounce of courage as you face off against countless\n"
              "pits and race against your own agony to capture the elusive....... \n\n"
              "*****  Four Pillars of Object-Oriented Programming *****\n")

    """This method describes the goal of the game, how to win, and the objects
    encountered during the game"""
    def how_to_play(self):
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

    """This method asks user for Character Name input. This should reference the
    Adventurer Class"""
    def create_adv(self):
        adv_name = input("Welcome to the bridge of death... What is your name? ")
        # pass char_name into Adventurer.char_name

    """This method will define the size of the dungeon array.  1 = 3x3, 2 = 5x5, 3 = 6x6"""
    def difficulty(self):
        low = 1
        high = 5
        level = int(input("What is your quest? Enter a difficulty from 1 (Easy) to 5 (Hard): "))
        if low <= level <= high:
            pass  # create dungeon & accordingly
        else:
            print("\nAhhhhhhhhhhhhh\' You were thrown in the gorge.  Game over.\n")
            return restart_game()

    """This bonus method will follow the Monty Python series of questions at the 
    Bridge of Death.  If the user inputs the appropriate arguments, the subsequent
    actions will take place."""
    # def monty():
    #     bonus = str(input("What is your favorite color? "))
    #     if bonus == str("I don't know."):
    #         print("\nAhhhhhhhhhhhhh\' You were thrown in the gorge.  Game over.")
    #     else:
    #         print("Right.  Off you go.")

    """This method will print the current room in the dungeon.  It will show any doors 
    or objects in the room."""
    def print_room(self):
        pass

    """This method will allow the user to perform a set of tasks based on the room and 
    inventory the adventurer holds:  Move, use healing/vision potion, view inventory, give up"""
    def user_input(self):
        pass

    """This method provides a hidden menu feature that prints out the entire dungeon
    for testing / easter egg purposes"""
    def hidden_menu(self):
        pass

    """This method prints the entire dungeon; to be used in hidden menu or at end of game"""
    def print_dungeon(self):
        pass


start_game()