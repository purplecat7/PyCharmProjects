"""
Main "actor" for Library
Assumes a LibrarySystem object with methods:

borrow_item(username_or_user_id, item_name_or_item_id, date = datetime.date.today())
return_item(username_or_user_id, item_name_or_item_id, date = datetime.date.today())
change_fine_of_user(fine_reduce_by, username = None, user_id = None)
is_item_available(item_identifier) # item identifier can be string (item_name) or integer (item_id)
add_new_item(item_type, item_name)
add_new_user(username)
find_fine_of_user(user_identifier, date = datetime.date.today()) # user identifier can be string (username) or integer (user_id)
can_user_borrow(user_identifier, date = datetime.date.today())
"""

import os.path as op
from LibSys import LibrarySystem
from item_initialise import  ItemInitialise
from user_initialise import UserInitialise
from item import Book, DVD, Journal
import datetime

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


libsys = LibrarySystem()
# instantiate Library System
item_init = ItemInitialise(libsys)
# instantiate Item Initialiser
user_init = UserInitialise(libsys)


def setup_libsys(initial_catalogue_dictionary):
    """
    Function to initially create a library system, optionally with a dictionary of items to initialise system with
    :param initial_catalogue_dictionary: dictionary of initial items. keys are filenames, arguments are the classes of
                                         the item within the given files
                                         example:- {top100t.txt: Book}
    :return: LibrarySystem object
    """
    #TODO this function is restricted to the loading of files which contain each only one subclass of item

    if initial_catalogue_dictionary:
        # if dictionary is non-empty

        for key in initial_catalogue_dictionary:

            item_init.load_items(filename = key, item_type = initial_catalogue_dictionary[key])
            # load items from specified file to the Library System

    return libsys


def all_scenario_user_setup():
    """
    Create users for test scenarios
    :param libsys: LibrarySystem object
    """
    user_init.add_new_user("JohnnyCodewarrior")
    user_init.add_new_user("JudyHacker")
    user_init.add_new_user("MissMarple")
    user_init.add_new_user("EricHalfbee")


def scenario1_setup(book_ident):
    """
    Johnny has one outstanding book, not overdue
    :param libsys: LibrarySystem object
    :param book_name: string, name of book; or integer, int
    """
    libsys.checkout("JohnnyCodewarrior", book_ident, datetime.date.today() - datetime.timedelta(days = 3))

def scenario1():
    """
    Run scenario 1 from CRC exercise on libsys
    :param libsys: LibrarySystem object
    """
    libsys.checkout("JohnnyCodewarrior", "Document, Your job depends on it")

def scenario2_setup(overdueJournalName, date_in_the_past, book_name,
                    earlier_date = datetime.date.today() - datetime.timedelta(days = 3)):
    """
    Setup for scenario 2, add Journal to system, and make it have been borrowed on some past date
    Give Judy f2 fine, and a book out (not overdue)
    :param libsys: LibrarySystem object
    :param overdueJournalName: string, name of Journal
    :param date_in_the_past: datetime object, date at which Journal was borrowed
    :param book_name: string, name of Book Judy has out
    :param earlier_date: datetime object, date at which Book was borrowed
    """
    item_init.load_new_item(libsys, Journal, overdueJournalName)
    item_init.load_new_item(libsys, DVD, "Debugging to music")
    libsys.checkout("JudyHacker", overdueJournalName, date_in_the_past)
    libsys.checkout("JudyHacker", book_name, earlier_date)
    libsys.change_fine_of_user("JudyHacker", fine_reduce_by = -2)
    # there needs to be some mechanism by which users can pay back fines, this should also be used to increase fines
    # for the sake of setting up these scenarios

def scenario2(overdueJournalName):
    """
    Run scenario 2 from CRC exercise on libsys
    :param libsys: LibrarySystem object
    :param overdueJournalName: string, name of Journal
    """
    libsys.return_item("JudyHacker", overdueJournalName)
    libsys.checkout("JudyHacker", "Debugging to music")


def scenario3():
    """
    Run scenario 3 from CRC exercise on libsys
    :param libsys: LibrarySystem object
    """
    is_journal_avail = libsys.is_item_available("Sleuthing in C#")

    if is_journal_avail:
        libsys.checkout("MissMarple", "Sleuthing in C#")


def scenario4_setup(item_list, list_of_past_dates):
    """
    Assign items in list to Eric, overdue, in libsys
    :param item_list: list of item objects
    :param list_of_past_dates: list of datetime objects of same length
    """
    for date_index, item in enumerate(item_list):
        libsys.checkout("EricHalfbee", item.name, list_of_past_dates[date_index])


def scenario4(item_list, dvd, eric_money):
    """
    Run scenario 4 from CRC exercise on libsys
    :param libsys: LibrarySystem object
    :param item_list: list of item objects that Eric has overdue
    :param dvd: DVD object Eric wants to borrow
    :param eric_money: float, amount of money Eric has
    """
    for item in item_list:

        libsys.return_item("EricHalfbee", item.name)
    # make Eric return all overdue items
    # this will internally increase his accrued fine accordingly

    eric_fine = libsys.find_fine_of_user("EricHalfbee")

    libsys.change_fine_of_user("EricHalfbee", fine_reduce_by= min(eric_fine, eric_money))
    # make Eric pay off as much of his fine as he can with the funds available

    can_Eric_borrow = libsys.can_user_borrow( "EricHalfbee")

    if can_Eric_borrow:

        libsys.checkout(libsys, "EricHalfbee", dvd.name)
        # if he can now borrow, do this

if __name__ == "__main__":
    libsys = setup_libsys({op.normpath("..\data\top100t.txt"): Book})
    all_scenario_user_setup()
    scenario1_setup( 5)
    scenario1()
    print("success")