# Credit: https://stackoverflow.com/questions/53783227/tkinter-overlaying-a-label-on-top-of-a-background-image
# Credit: https://stackoverflow.com/questions/17779540/python-how-to-get-an-entry-box-within-a-message-box

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from dungeon import Dungeon

my_name = ''


def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    bk_photo = ImageTk.PhotoImage(image)

    label.config(image=bk_photo)
    label.image = bk_photo  # avoid garbage collection


def what_is_your_name():
    global my_name
    my_name = askstring('THE Dungeon OF Doom', 'What is your name?')

    # if name == '':
    #     name = "You didn't give us you name"
    # showinfo('THE Dungeon OF Doom', 'Hi, {}'.format(name))


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


root = Tk()
root.title("Title")
root.geometry('800x800')
root.title("THE Dungeon OF Doom by Jeff-Dee-Kishan")

intro = "Welcome to the Dungeon of Doom!  Prepare for the most difficult\n" \
        "challenge of your adventure-seeking life.  Check your pride at the door,\n" \
        "and bring an extra ounce of courage as you face off against countless\n" \
        "pits and race against your own agony to capture the elusive.......\n" \
        "*****  Four Pillars of Object-Oriented Programming *****"

frame = Frame(root, relief='raised', borderwidth=2)
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

# ---------------- button --------------------
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)
start_button = Button(center_frame, text="Let's the game begin...", bg='blue', command=what_is_your_name)

start_button.pack(side=BOTTOM)

howto_button = Button(center_frame, text="How to play...", bg='green', command=how_to)
howto_button.pack(side=BOTTOM)

# Label(center_frame, text=intro, width=60).pack()
maze_label = Label(root)
maze = Dungeon(5, 5, 0, 0)
# font=("Courier New", 16, "italic")
# Label.configure(font=("Courier New", 16, "bold"))
Label(center_frame, text=maze, width=60).pack()

root.mainloop()

