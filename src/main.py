# coding=utf-8
"""
NAME
    main - library system program
FILE
    main.py
CLASSES
    NumID
"""
import item_init as im
import userinit as um
import library_manager
import datetime as dt


class NumbID:
    """
    Utility class to provide unique identifier.

    Methods defined here:
        new_id(...)
            Provide next unique identifier, starts at 1.

        reset_id(...)
            Reset unique identifier.
    """
    id_number = 0

    def __init__(self):
        pass

    def __del__(self):
        pass

    # note that these use the @staticmethod adornment since no instance
    # attributes are used.
    @staticmethod
    def new_id():
        NumbID.id_number += 1
        return NumbID.id_number

    @staticmethod
    def reset_id():
        NumbID.id_number = 0


def create_library_catalogue(lib_controller, infile):
    """
    Populate library's list of loanable items.

    :param lib_controller: LibraryController object
    :param infile: text file containing book titles
    :return: no return
    """
    item_manager = im.ItemManager()
    item_manager.set_library_controller(lib_controller)
    file_ = open(infile, 'r')
    for line in file_:
        item_manager.create_book(line.strip(), NumbID.new_id())
    print ('Number of books added: ', NumbID.id_number)
    item_manager.create_journal("Amazing Clouds", NumbID.new_id())
    item_manager.create_journal("Sleuthing in C#", NumbID.new_id())
    item_manager.create_dvd("Dad's Army", NumbID.new_id())
    item_manager.create_dvd("Debugging to music", NumbID.new_id())
    print ('Total number of items: ', NumbID.id_number)


def create_library_members(lib_controller):
    """
    Create some users for the library system's list.

    :param lib_controller: LibraryController object
    :return: no return
    """
    user_manager = um.UserInit()
    user_manager.set_library_controller(lib_controller)
    NumbID.reset_id()
    # create 4 users
    for count in range(0, 4):
        user_manager.create_user(NumbID.new_id())
        print ('User ID created: ', NumbID.id_number)


def exercise1(user_id, title, lib_controller):
    """
    Checkout an item.

    :param user_id: user's unique identifier
    :param title: item to borrow
    :param lib_controller: LibraryController object
    :return: no return
    """
    lib_controller.checkout(user_id, title)


def exercise2(user_id, return_id, title, lib_controller):
    """
    Return an item and checkout another.

    :param user_id: user's unique identifier
    :param return_id: unique id of item returned
    :param title: item to borrow
    :param lib_controller: LibraryController object
    :return: no return
    """
    fine = lib_controller.user_fine(user_id)
    print ("User: ", user_id)
    print ("Total Fine: ", fine)
    
    lib_controller.return_item(user_id, return_id)
    lib_controller.checkout(user_id, title)


def johnny_codewarrior(lib_controller):
    """What happens when Johnny Codewarrior, who has no accrued fines and one
    outstanding book, not overdue, checks out a book entitled Document, Your
    job depends on it."""
    user_id = NumbID()
    # One outstanding book
    date = dt.datetime(2018, 06, 01, 12, 56, 07)
    lib_controller.checkout(user_id,
                            'Harry Potter and the Prisoner of Azkaban', date)
    # Checks out new book
    lib_controller.checkout(user_id, 'Document, Your job depends on it')


def main():
    """
    Program initialisation and execution.
    :return: no return
    """
    print ("Initialising library controller...")
    lib_controller = library_manager.LibMgr()

    print ("Populating library catalogue...")
    infile = 'top100t.txt'
    try:
        create_library_catalogue(lib_controller, infile)
    except:
        print ("Catalogue populating failed")
        raise

    print ("Populating library members...")
    try:
        create_library_members(lib_controller)
    except:
        print ("User populating failed")
        raise

    print ("Exercise 1...")
    try:
        exercise1(1, 'The Kite Runner', lib_controller)
    except:
        print ("Exercise 1 failed")
        raise

    print ("Exercise 2...")
    try:
        exercise2(1, 19, 'Sleuthing in C#', lib_controller)
    except:
        print ("Exercise 2 failed")
        raise

    print ("Johnny Codewarrior")
    try:
        johnny_codewarrior(lib_controller)
    except:
        print "Johnny codewarrior failed"
        raise
    

if __name__ == '__main__':
    main()
