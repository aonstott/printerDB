import sqlite3
from database import Printer
import sys
#connect to database

#set up main function with command line arguments
printer = Printer()

def __main__():
    if printer.is_empty():
        printer.initialize_db()
        print("Database initialized")
    if len(sys.argv) == 1:
        print("Please enter a command")
    
    elif sys.argv[1] == "add":
        if len(sys.argv) == 4:
            printer.add_printer(sys.argv[2], sys.argv[3])
            print("Printer added")
        else:
            print("Please enter a location and model")

    elif sys.argv[1] == "remove":
        if len(sys.argv) == 3:
            printer.remove_printer(sys.argv[2])
            print("Printer removed")
        else:
            print("Please enter a location")
    
    elif sys.argv[1] == "cleardb":
        printer.clear_db()
        print("Database cleared why would you do this")
    
    elif sys.argv[1] == "printdb":
        printer.print_db()

    elif sys.argv[1] == "setlastinspected":
        if len(sys.argv) == 4:
            printer.set_last_inspected(sys.argv[2], sys.argv[3])
            print("Last inspected date set")
        else:
            print("Please enter a location and date")


__main__()

        
