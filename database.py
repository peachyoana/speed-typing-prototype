import sqlite3
"""
Show Stats should be ordered by ascending order of 'when'
This would be done as the format will be YYYY-MM-DD HH:MM
^^^^ This will be sorted in the correct order in the csv file

then the statement may be 'SELECT * FROM stats WHERE username = {username} ORDER BY 'when' ASC' 


"""

def create_db():

    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE User (
                 user_id text PRIMARY_KEY, 
                 username text,
                 )""")

    c.execute("""CREATE TABLE Stats (
                 username text,
                 wpm real,
                 chpm real,
                 time_for_attempt BLOB,
                 real_time BLOB,
                 accuracy real, 
                 score real
                 )""")

    c.execute("""CREATE TABLE Texts (
                     text_id text,
                     text text, 
                     genre text
                     )""")

    c.execute("""CREATE TABLE UsedText (
                     username text FOREIGN_KEY,
                     text_id text FOREIGN_KEY
                     )""")

    c.execute("""INSERT INTO User(username) values ("peachyoana")""")

    for r in result:
        print(r)

    conn.commit()
    conn.close()


def show_stats():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM stats")
    items = c.fetchall()

    for item in items:
        """ Add the corresponding numbers of item[] in the 'form' placeholders """
        form = "Username: {} \t WPM: {} \t CHPM: {} \t Accuracy: {} \t Time Taken: {} \t Time of Attempt: {} \tScore: {}"
        print(form.format(item[0], item[1], item[2], item[3], item[4]))

    conn.commit()
    conn.close()


def add_one(username, wpm, chpm, accuracy, time_for_attempt, real_time, score):
    """ Since the times would have to be a BLOB format you have to create
        separate sub-programs for them with placeholders using datetime """

    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("INSERT INTO")
    items = c.fetchall()

    conn.commit()
    conn.close()


def get_csv(username):
    """ Fetches all records in the database with that username
        ordered by BLOB data type in 'When' field
    https://www.geeksforgeeks.org/writing-csv-files-in-python/
    """
    import csv
    from datetime import date

    # today's date so that if multiple csv files
    # are downloaded they can differentiate between them
    today = date.today()

    conn = sqlite3.connect("data.db") # create connection to database
    c = conn.cursor() # create a cursor

    form = c.execute("SELECT * FROM stats WHERE username = (?) ORDER BY when ASC", (username,)) # create a readable string
    items = c.fetchall()

    for item in items:
        with open("stats-{}-{}.csv".format(username, today.strftime("%b-%d-%Y")), "w") as user_csv:
            csv_writer = csv.writer(user_csv)
            # writing the fields
            csv_writer.writerow() # insert an array of the 'items'

    conn.commit()
    conn.close()