import sqlite3
import pandas as pd

# Connect to or create a database (this will create a new file if it doesn't exist)
#THIS WILL CLEAR ALL DB INFO DON'T RUN UNLESS YOU WANT TO CLEAR THE DB


class Printer:
    def initialize_db(self):
        conn = sqlite3.connect('printers.db')
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Create a table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS printers (
                id INTEGER PRIMARY KEY,
                Location TEXT,
                Model TEXT,
                Last_inspected TEXT
            )
        ''')

        # Insert data into the table
        #cursor.execute("INSERT INTO printers (Location, Model, Last_cleaned) VALUES (?, ?, ?)", ('test_room', 'HP 6000', '12/25/1994'))



        # Print the data
        cursor.execute('DELETE FROM printers')
        df = pd.read_csv('printer_list.csv')


        # Insert data into the table

        for i in range(len(df)):
            cursor.execute("INSERT INTO printers (Location, Model) VALUES (?, ?)", (df['Locations'][i], df['Model'][i]))

        # Commit the changes and close the connection


        conn.commit()
        conn.close()

    def add_printer(self, location, model):
        conn = sqlite3.connect('printers.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO printers (Location, Model) VALUES (?, ?)", (location, model))
        conn.commit()
        conn.close()

    def remove_printer(self, location):
        conn = sqlite3.connect('printers.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM printers WHERE Location = ?", (location,))
        conn.commit()
        conn.close()

    def clear_db(self):
        conn = sqlite3.connect('printers.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM printers")
        conn.commit()
        conn.close()

    def print_db(self):
        conn = sqlite3.connect('printers.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM printers")
        print(cursor.fetchall())
        conn.commit()
        conn.close()

    def set_last_inspected(self, location, date):
        conn = sqlite3.connect('printers.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE printers SET Last_inspected = ? WHERE Location = ?", (date, location))
        conn.commit()
        conn.close()

    def clear_last_inspected(self, location):
        conn = sqlite3.connect('printers.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE printers SET Last_inspected = ? WHERE Location = ?", ('', location))
        conn.commit()
        conn.close()
    
    def clear_all_least_inspected(self):
        conn = sqlite3.connect('printers.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE printers SET Last_inspected = ?", ('',))
        conn.commit()
        conn.close()

    def is_empty(self) -> bool:
        conn = sqlite3.connect('printers.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM printers")
        if cursor.fetchall() == []:
            conn.commit()
            conn.close()
            return True
        else:
            conn.commit()
            conn.close()
            return False

