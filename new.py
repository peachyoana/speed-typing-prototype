# -------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      gw15kolevaioana
#
# Created:     04/03/2021
# Copyright:   (c) gw15kolevaioana 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------
"""
Link to database with tables:
    User:
        id
        username

    Stats:
        id - PK (date + first 3 letters of username + real time without separations
                e.g 27032003ION100920) # no
        username - fk
        wpm
        chpm
        real_time
        attempt_time
        accuracy

    Texts:
        id
        text
        genre

    UsedTexts:
        username - fk
        texts - fk

"""

"""
Establish link to the database before the loop

Before loop:
    import sqlite3
    connection = sqlite3.connect("name.db")
    cursor = connection.cursor()

During loop:
    Everything with cursor
    e.g cursor.execute("create table table1
                        (int id not not null auto_increment primary key,
                        varchar(50) fullname not null")

After loop:
    connection.commit()
    connection.close()

"""
"""

text = " ..................... "
words = text.split(" ")
len(words)

"""

from tkinter import *
from time import *
import time, datetime, random
import database

"""
User class that stores username
Have a GUI class:
    Menu
    Buttons
    Widgets/Boxes
    Texts

User class:
    Username
    Statistics

Main Program:
    Calculate user inputs and add them to statistics
    Export to database
"""

""" Use main program functions to calculate stuff,
    get username through gui class,
    do user = User(...)
    pass that stuff into database

    OR pass the stuff to database through User class
    real time - should come from GUI.clock()
    time_for_attempt - should come from GUI.timer()
    wpm, chmp, accuracy all relate to GUI.interaction_boxes()
    username relates to GUI.get_user()
"""


"""
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry.html
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/text-index.html
https://tkdocs.com/tutorial/text.html

mark_set(mark, index) - update this every time a user moves to the right or the left
of the current index.

If I backspace or arrow to the left or up that will be moving back
If I enter, space, right arrow or down arrow, that will be moving forward

Finish the timer
make it so that it starts when the person starts typing,
and when you press 'Press me to Start'
"""


# so that you don't create a new db everytime u run the program

class User:
    def __init__(self, username, wpm, chpm, time_for_attempt, real_time, accuracy, score):
        self.username = username
        self.wpm = wpm
        self.chpm = chpm
        self.time_for_attempt = time_for_attempt
        self.real_time = real_time
        self.accuracy = accuracy
        self.score = score

    def get_username(self):
        pass


class GUI:
    def __init__(self, master, text):
        self.master = master
        self.text = text
        self.menubar = Menu(master)  # initiate menu template
        self.optionsmenu = Menu(self.menubar)  # initiate options menu
        self.helpmenu = Menu(self.menubar, tearoff=0)  # initiate help menu

        # screen stats
        self.x = 800
        self.y = 600

        self.monitor_width = root.winfo_screenwidth()
        self.monitor_height = root.winfo_screenheight()

        self.get_user(self.x, self.y,
                      self.monitor_width, self.monitor_height)

        self.place_on_screen(self.x, self.y,
                             self.monitor_width, self.monitor_height)
        self.interaction_boxes()  # should take in text
        self.set_background()
        self.create_menu()
        self.buttons()
        self.labels()
        self.clock()
        self.timer()

        self.master.title("Speed Typing Game")  # name the main window
        self.master.mainloop()

    def place_on_screen(self, x, y, width, height):
        # get user monitor width and height

        # find centre of monitor so that it is consistent centre
        # placement on any resolution
        pos_horizontally = int((self.monitor_width / 2) - (self.x / 2))
        pos_vertically = int((self.monitor_height / 2) - (self.y / 2))
        self.master.geometry("%dx%d+%d+%d" % (self.x, self.y, pos_horizontally, pos_vertically))
        self.master.attributes('-topmost', False)

    def set_background(self):
        self.master['background'] = '#617D6F'  # set background colour

    def labels(self):
        self.title_label = Label(self.master, text="SPEED TYPING GAME")
        self.title_label.place(height=35, width=200, relx=0.5, rely=0.09, anchor='center')

    def create_menu(self):
        def _optionsmenu_restart():
            """ Restarts the text, attempt time and clears input box and sets index to 0 """
            self.input_box.delete(1.0, END)
            pass

        def _optionsmenu_save():
            self.helpindex = Toplevel(self.master)
            self.helpindex.title("Save")
            self.helpindex.geometry("300x500")

        def _optionsmenu_changeusername():
            """ Will allow user to switch username to either already existing user or
            a new one """

            self.helpindex = Toplevel(self.master)
            self.helpindex.title("Change Username")
            self.helpindex.geometry("300x500")

        def _optionsmenu_change_genre():
            """ Opens a new box that allows to change genre or opens the """
            self.helpindex = Toplevel(self.master)
            self.helpindex.title("Change Genre")
            self.helpindex.geometry("300x500")

        def _helpmenu_helpindex():
            """ A new window that gives brief description about the program and how to use it"""
            self.helpindex = Toplevel(self.master)
            self.helpindex.title("Help Index")
            self.helpindex.geometry("300x500")

        def _helpmenu_about():
            """ A new window that gives a brief description about the program and its version, author and rights """
            self.helpindex = Toplevel(self.master)
            self.helpindex.title("About")
            self.helpindex.geometry("500x300")
            self.helpindex.label()

        self.optionsmenu.add_command(label="Restart", command=_optionsmenu_restart)
        self.optionsmenu.add_command(label="Save", command=_optionsmenu_save)
        self.optionsmenu.add_command(label="Change username", command=_optionsmenu_changeusername)
        self.optionsmenu.add_command(label="Change text genre...", command=_optionsmenu_change_genre)
        self.optionsmenu.add_separator()
        self.optionsmenu.add_command(label="Exit", command=self.master.destroy)
        self.menubar.add_cascade(label="Options", menu=self.optionsmenu)

        self.helpmenu.add_command(label="Help Index", command=_helpmenu_helpindex)
        self.helpmenu.add_command(label="About...", command=_helpmenu_about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.master.config(menu=self.menubar)

    def interaction_boxes(self):
        def text_box():
            self.text_box = Text(self.master,
                                 font=('Arial', 12),
                                 bg="#F8F8FF",
                                 wrap=WORD)

            self.text_box.place(height=130, width=300, relx=0.5, rely=0.3, anchor='center')
            self.text_box.insert('0.0', self.text)  # selects a random paragraph by default
            self.text_box.config(state=DISABLED)  # read-only

        def entry_box():
            self.input_box = Text(self.master, font=('Arial', 12), bg="#F8F8FF")
            self.input_box.place(height=30, width=300, relx=0.5, rely=0.5, anchor='center')

        text_box()
        entry_box()

    def buttons(self):
        def start():
            self.text_box.delete(1.0, END)

        def restart():
            self.input_box.delete(1.0, END)

        def _genre_button():
            """ Research and add more options"""
            OPTIONS = [
                "Article",
                "Paragraph",
                "Lyrics"
            ]

            self.genre_button = StringVar(self.master)
            self.genre_button.set("Paragraph")  # default value

            dropdown = OptionMenu(self.master, self.genre_button, "Genre", *OPTIONS)
            dropdown.place(height=30, width=100, relx=0.63, rely=0.6, anchor='center')

            """
            Everytime they choose a different genre the program should randomize a text
            from that genre making a link to the database
            """

        self.start_button = Button(self.master, text="Press me to start", command=start)
        self.start_button.place(height=30, width=100, relx=0.37, rely=0.6, anchor='center')

        self.restart_button = Button(self.master, text="Restart", command=restart)
        self.restart_button.place(height=30, width=100, relx=0.5, rely=0.6, anchor='center')

        self.genre_button = Button(self.master, text="Genre", command=_genre_button)
        self.genre_button.place(height=30, width=100, relx=0.63, rely=0.6, anchor='center')

        self.close_button = Button(self.master, text="Exit", command=self.master.destroy)
        self.close_button.place(height=30, width=60, relx=0.92, rely=0.92, anchor='center')

    def clock(self):
        def update_clock():
            now = datetime.datetime.now()
            self.time_label.configure(text=now.strftime("%H:%M:%S"))
            self.master.after(1000, update_clock)

        def get_attempt_start_time():
            """ Once the person has started typing get a timestamp
                of the HH:MM and pass it back"""
            pass

        self.time_label = Label(self.master)
        self.time_label.place(height=35, width=100, relx=0.93, rely=0.04, anchor='center')
        update_clock()

    def timer(self):
        # https://www.geeksforgeeks.org/create-stopwatch-using-python/
        counter = 66600
        running = False

        def counter_label(label):
            def count():
                if running:
                    global counter

                    # To manage the intial delay.
                    if counter == 66600:
                        display = "Starting..."
                    else:
                        tt = datetime.fromtimestamp(counter)
                        string = tt.strftime("%H:%M:%S")
                        display = string

                    label.config(text=display)
                    label.after(1000, count)
                    counter += 1

            # Triggering the start of the counter.
            count()

        label = Label(self.master)
        label.place(height=35, width=100, relx=0.07, rely=0.04, anchor='center')
        counter_label(label)

    def get_user(self, x, y, width, height):
        """ Add an Enter button for user to confirm their username
            once pressed this is taken as an input and the method returns it
            use it in main program and send it to """

        """ Add a warning window that notifies the player that a username already exists
            and whether they will still want to proceed """

        def enter():
            """ Hey new user! / Welcome back, <username>! Your last attempt was on... """
            pass

        def raise_above_all(window):
            window.attributes('-topmost', 1)

        def username_exists():
            """ If username exists..."""
            username_exists_box = Tk()
            username_exists_box.title("Player already exists")

        username_box = Tk()  # figure out why parent window closes as well
        username_box.title("Player Username")
        username_box['background'] = '#8cab9c'

        # placing the box
        x, y = 300, 400  # box width and height
        pos_horizontally = int(self.monitor_width / 2 - (x / 2))  # you don't want it in the middle of the screen
        pos_vertically = int(self.monitor_height / 2 - (y / 2))  # but in the middle self.master
        res = "{}x{}+{}+{}"
        username_box.geometry(res.format(x, y, pos_horizontally, pos_vertically))  # pos in the middle of the screen

        # widgets
        label_text = "Username must be between 3-15 characters \nValid characters: a-z 0-9 _&$£-.\nPlease enter your username:\n"
        label = Label(username_box, wraplength=180, justify="center", bg='#617D6F', fg="#ffffff", text=label_text)
        label.place(height=200, width=180, relx=0.5, rely=0.4, anchor='center')

        input_box = Text(username_box, font=('Arial', 12), bg="#F8F8FF")
        input_box.place(height=25, width=120, relx=0.5, rely=0.5, anchor='center')

        enter_button = Button(username_box, text="Enter", command=enter)
        enter_button.place(height=30, width=80, relx=0.5, rely=0.6, anchor='center')

        exit_button = Button(username_box, text="Exit", command=username_box.destroy)
        exit_button.place(height=30, width=60, relx=0.5, rely=0.7, anchor='center')
        """ You have to do username restrictions:
                isalnum(), &, %, _  <- use regex
                lenght: 3-15

                https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/

        convert it to lowercase
        """
        raise_above_all(username_box)


"""
Have a function that gets text from database and pass it in
into text box widget in the gui class
"""

root = Tk()
my_gui = GUI(root, "TEXT")