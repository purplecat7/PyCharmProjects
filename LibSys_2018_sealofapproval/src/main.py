# coding=utf-8
"""
NAME
    main - library system program
FILE
    main.py
CLASSES
    NumID
"""
from __future__ import print_function
import item_init as im
import userinit as um
import library_manager
import datetime as dt
from  except_item_not_available import ItemNotAvailableError


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
    item_manager = im.ItemInit()
    item_manager.set_library_manager(lib_controller)
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

    lib_controller.return_item(user_id, return_id)
    lib_controller.checkout(user_id, title)


def johnny_codewarrior(lib_controller):
    """What happens when Johnny Codewarrior, who has no accrued fines and one
    outstanding book, not overdue, checks out a book entitled Document, Your
    job depends on it."""
    user_id = 1
    # One outstanding book
    date = dt.datetime(2018, 06, 01, 12, 56, 07)
    lib_controller.checkout(user_id,
                            'Harry Potter and the Prisoner of Azkaban', date)
    # Checks out new book
    lib_controller.checkout(user_id, 'Document, Your job depends on it')


def judy_hacker(user_id, return_id, lib_controller):
    """What happens when Judy Hacker, who has 2 pounds oustanding
    fines and one outstanding book, not overdue,
    checks out a DVD entitled 'Debugging to music' and
    is bringing back an overdue journal."""
    # One outstanding book
    date = dt.datetime(2018, 06, 03, 11, 30, 00)
    lib_controller.checkout(user_id, 'Chocolat', date)
    # Checks out new book
    lib_controller.checkout(user_id, 'Debugging to music')
    # is bringing back an overdue journal
    lib_controller.return_item(user_id, return_id)


def miss_marple(lib_controller):
    """
    Miss Marple wants to borrow "Sleuthing in C#"
    :param lib_controller: lib_controller object
    :return:
    """
    checked_out_user = 4
    lib_controller.checkout(checked_out_user,"Amazing Clouds")
    #try to check out the item for Miss MArple
    try:
        lib_controller.checkout(3, "Amazing Clouds")

    except ItemNotAvailableError as e: #it should raise this exception
        print(e.message)



# def eric_halfbee(lib_controller):
#     user_id = 4
#     date = dt.datetime(2018, 06, 03, 11, 30, 00)
#     #has some overdue books
#     lib_controller.checkout(user_id,"New Moon", date)
#     lib_controller.checkout(user_id, "The Lovely Bones", date)
#     lib_controller.checkout(user_id, "The Curious Incident of the Dog in the Night-time", date)
#     lib_controller.checkout(user_id, "The Time Traveler's Wife", date)
#     #returns the pile of books
#     lib_controller.returnitem(user_id,"New Moon")
#     lib_controller.returnitem(user_id, "The Lovely Bones")
#     lib_controller.returnitem(user_id, "The Curious Incident of the Dog in the Night-time")
#     lib_controller.returnitem(user_id, "The Time Traveler's Wife")
#     #Find the fines
#     lib_controller.getuserfines(user_id)
#     # ToDo pay fines if he has enough
#     #




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
        print ("Johnny codewarrior failed")
        raise

    print ("Judy Hacker")
    try:
        judy_hacker(1, 1, lib_controller)
    except:
        print ("Judy Hacker failed")
        raise

    print ("Miss Marple")
    try:
        miss_marple(lib_controller)
    except:
        print ("Miss Marple failed to solve the crime")
        raise
    

if __name__ == '__main__':
    main()
