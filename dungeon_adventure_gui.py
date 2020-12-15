# Credit: https://stackoverflow.com/questions/53783227/tkinter-overlaying-a-label-on-top-of-a-background-image
# Credit: https://stackoverflow.com/questions/17779540/python-how-to-get-an-entry-box-within-a-message-box

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from dungeon import Dungeon


class DungeonAdventure:

    def __init__(self):
        self.__user_name = ''
        self.__root = Tk()
        self.__root.title("Title")
        self.__root.geometry('600x700')
        self.__root.title("THE Dungeon OF Doom by Jeff-Dee-Kishan")

    def user_name(self):
        return self.__user_name

    def introduction(self):

        def resize_image(event):
            new_width = event.width
            new_height = event.height

            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)

            label.config(image=photo)
            label.image = photo  # avoid garbage collection

        def what_is_your_name():
            self.__user_name = askstring('THE Dungeon OF Doom', 'What is your name?')
            if self.__user_name is None:
                showinfo('THE Dungeon OF Doom', "Don't be shy. Name is required to the start the game !!!")
            else:
                showinfo('THE Dungeon OF Doom', 'Hello, {}. Welcome to THE DUNGEON OF DOOM'.format(self.__user_name))

        def how_to():
            how = "The goal of this game is to escape the dungeon maze after finding the\n" \
                  "four pillars:\n" \
                  "   1: Abstraction\n" \
                  "   2: Encapsulation\n" \
                  "   3: Inheritance\n" \
                  "   4: Polymorphism\n\n" \
                  "Be warned - you have limited health points [HP]. If you fall in a pit, you\n" \
                  "will lose HP. Don't fret - there are also Healing Potions and Vision\n" \
                  "Potions scattered about the dungeon to help you in your quest. Once you\n" \
                  "collect all Four Pillars of OO, the exit door will unlock --- if you reach\n" \
                  "the exit before your HP reaches a big fat zero, you win!\n\n" \
                  "You can move throughout the map by typing \'u\', \'d\', \'l\', or \'r\'\n" \
                  "You can only move through the doors that exist in the dungeon.\n\n" \
                  "Be strong in your journey...\n\"Even death is not to be feared by one who " \
                  "has lived wisely\" --- Buddha\n"
            messagebox.showinfo("THE Dungeon OF Doom", how)

        intro = "Welcome to the Dungeon of Doom!  Prepare for the most difficult\n" \
                "challenge of your adventure-seeking life.  Check your pride at the door,\n" \
                "and bring an extra ounce of courage as you face off against countless\n" \
                "pits and race against your own agony to capture the elusive.......\n" \
                "*****  Four Pillars of Object-Oriented Programming *****"

        frame = Frame(self.__root, relief='raised', borderwidth=2)
        frame.pack(fill=BOTH, expand=YES)
        frame.pack_propagate(False)

        copy_of_image = Image.open("wizard.jpg")
        photo = ImageTk.PhotoImage(copy_of_image)

        label = Label(frame, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', resize_image)

        center_frame = Frame(frame, relief='raised', borderwidth=2)
        center_frame.place(relx=.5, rely=.5, anchor=CENTER)

        # ---------------- introduction -----------------
        Label(center_frame, text=intro, width=60).pack()
        # ------------- button - -------------------
        bottom_frame = Frame(self.__root)
        bottom_frame.pack(side=BOTTOM)
        start_button = Button(center_frame, text="Let's the game begin...", bg='blue', command=what_is_your_name)

        start_button.pack(side=BOTTOM)

        howto_button = Button(center_frame, text="How to play...", bg='green', command=how_to)
        howto_button.pack(side=BOTTOM)

        # ---------------- Get: Player Name --------------------
        # my_label = Label(center_frame, text="Enter you name:")
        # my_label.pack(side=BOTTOM)
        # ---------------- How to play the game --------------------
        # howto_button = Button(center_frame, text="How to play...", bg='green', command=how_to)
        # howto_button.pack(side=BOTTOM)
        # ---------------- Start the Game --------------------
        # my_box = Entry(center_frame)
        # my_box.pack(side=BOTTOM)
        # bottom_frame = Frame(self.__root)
        # bottom_frame.pack(side=BOTTOM)
        # start_button = Button(center_frame, text="Let's the game begin...", bg='blue', command=what_is_your_name)
        # start_button.pack(side=BOTTOM)

        self.__root.mainloop()

    def create_a_maze(self):

        def resize_image(event):
            new_width = event.width
            new_height = event.height

            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)

            label.config(image=photo)
            label.image = photo  # avoid garbage collection

        frame = Frame(self.__root, relief='raised', borderwidth=2)
        frame.pack(fill=BOTH, expand=YES)
        frame.pack_propagate(False)

        copy_of_image = Image.open("Maze.jpg")
        photo = ImageTk.PhotoImage(copy_of_image)

        label = Label(frame, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.bind('<Configure>', resize_image)

        center_frame = Frame(frame, relief='raised', borderwidth=2)
        center_frame.place(relx=.5, rely=.5, anchor=CENTER)

        maze_label = Label(self.__root)
        maze = Dungeon(5, 5, 0, 0)
        Label(center_frame, text=maze, width=60, bg='yellow').pack()

        my_box = Entry(center_frame, bg='blue')
        my_box.pack(side=BOTTOM)
        bottom_frame = Frame(self.__root)
        bottom_frame.pack(side=BOTTOM)

        self.__root.mainloop()


da = DungeonAdventure()
da.introduction()
# if da.user_name() is not None:
#     da.create_a_maze()
# da.create_a_maze()



