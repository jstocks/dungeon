"""This method starts the game.  Provides an introduction and how to play guide.
It also kicks off the game with character name and difficulty."""
def start_game():
    intro()
    how_to_play()
    char_name()
    difficulty()

"""This method restarts the game if """
def restart_game():
    char_name()
    difficulty()

def intro():
    print("Welcome to the Dungeon of Doom!  Prepare for the most difficult \n"
          "challenge of your adventure-seeking life.  Check your pride at the door,\n"
          "and bring an extra ounce of courage as you face off against countless\n"
          "pits and race against your own agony to capture the elusive....... \n\n"
          "*****  Four Pillars of Object-Oriented Programming *****\n")


def how_to_play():
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
          "Be strong in your journey...\n\"Even death is not to be feared by one who "
          "has lived wisely\" --- Buddha\n")

def char_name():
    char_name = input("Welcome to the bridge of death... What is your name? ")
    # pass char_name into Adventurer.char_name

def difficulty():
    low = 1
    high = 5
    level = int(input("What is your quest? Enter a difficulty from 1 (Easy) to 5 (Hard): "))
    if low <= level <= high:
        pass  # create dungeon & accordingly
    else:
        print("\nAhhhhhhhhhhhhh\' You were thrown in the gorge.  Game over.\n")
        return restart_game()

# def monty():
#     bonus = str(input("What is your favorite color? "))
#     if bonus == str("I don't know."):
#         print("\nAhhhhhhhhhhhhh\' You were thrown in the gorge.  Game over.")
#     else:
#         print("Right.  Off you go.")

def print_room():
    pass

def user_input():
    pass
start_game()