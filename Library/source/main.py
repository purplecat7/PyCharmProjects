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

from LibSys import libsys as LibrarySystem
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



def setup_libsys(initial_catalogue_dictionary):
    """
    Function to initially create a library system, optionally with a dictionary of items to initialise system with
    :param initial_catalogue_dictionary: dictionary of initial items. keys are filenames, arguments are the classes of
                                         the item within the given files
                                         example:- {top100t.txt: Book}
    :return: LibrarySystem object
    """
    #TODO this function is restricted to the loading of files which contain each only one subclass of item

    libsys = LibrarySystem()
    # instantiate Library System

    item_init = ItemInitialise(libsys)
    # instantiate Item Initialiser

    if initial_catalogue_dictionary:
        # if dictionary is non-empty

        for key in initial_catalogue_dictionary:

            item_init.load_items(filename = key, item_type = initial_catalogue_dictionary[key])
            # load items from specified file to the Library System

    return libsys


def all_scenario_user_setup(libsys):
    """
    Create users for test scenarios
    :param libsys: LibrarySystem object
    """
    user_init = UserInitialise(libsys)

    user_init.add_new_user("JohnnyCodewarrior")
    user_init.add_new_user("JudyHacker")
    user_init.add_new_user("MissMarple")
    user_init.add_new_user("EricHalfbee")


def scenario1_setup(libsys, book_ident):
    """
    Johnny has one outstanding book, not overdue
    :param libsys: LibrarySystem object
    :param book_name: string, name of book; or integer, int
    """
    libsys.borrow_item(libsys, "JohnnyCodewarrior", book_ident, datetime.date.today() - datetime.timedelta(days = 3))


def scenario1(libsys):
    """
    Run scenario 1 from CRC exercise on libsys
    :param libsys: LibrarySystem object
    """
    libsys.borrow_item(libsys, "JohnnyCodewarrior", "Document, Your job depends on it")


def scenario2_setup(libsys, item_init, overdueJournalName, date_in_the_past, book_name,
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
    libsys.borrow_item("JudyHacker", overdueJournalName, date_in_the_past)
    libsys.borrow_item("JudyHacker", book_name, earlier_date)
    libsys.change_fine_of_user("JudyHacker", fine_reduce_by = -2)
    # there needs to be some mechanism by which users can pay back fines, this should also be used to increase fines
    # for the sake of setting up these scenarios


def scenario2(libsys, overdueJournalName):
    """
    Run scenario 2 from CRC exercise on libsys
    :param libsys: LibrarySystem object
    :param overdueJournalName: string, name of Journal
    """
    libsys.return_item(username = "JudyHacker", item_name = overdueJournalName)
    libsys.borrow_item("JudyHacker", None, "Debugging to music", None)


def scenario3(libsys):
    """
    Run scenario 3 from CRC exercise on libsys
    :param libsys: LibrarySystem object
    """
    is_journal_avail = libsys.is_item_available(item_name = "Sleuthing in C#")

    if is_journal_avail:
        libsys.borrow_item(libsys, username="MissMarple", item_name="Sleuthing in C#")


def scenario4_setup(libsys, item_list, list_of_past_dates):
    """
    Assign items in list to Eric, overdue, in libsys
    :param libsys: LibrarySystem object
    :param item_list: list of item objects
    :param list_of_past_dates: list of datetime objects of same length
    """
    for date_index, item in enumerate(item_list):
        libsys.borrow_item(libsys, "EricHalfbee", None, item.name, item.id, list_of_past_dates[date_index])


def scenario4(libsys, item_list, dvd, eric_money):
    """
    Run scenario 4 from CRC exercise on libsys
    :param libsys: LibrarySystem object
    :param item_list: list of item objects that Eric has overdue
    :param dvd: DVD object Eric wants to borrow
    :param eric_money: float, amount of money Eric has
    """
    for item in item_list:

        libsys.return_item(libsys, "EricHalfbee", None, item.name, item.id)
    # make Eric return all overdue items
    # this will internally increase his accrued fine accordingly

    eric_fine = libsys.find_fine_of_user(username = "EricHalfbee")

    libsys.change_fine_of_user(username="EricHalfbee", fine_reduce_by= min(eric_fine, eric_money))
    # make Eric pay off as much of his fine as he can with the funds available

    can_Eric_borrow = libsys.can_user_borrow(username = "EricHalfbee", user_id = None)

    if can_Eric_borrow:

        libsys.borrow_item(libsys, "EricHalfbee", None, dvd.name, dvd.id)
        # if he can now borrow, do this



# ### defunct
#
# def add_new_item(libsys, item_type, name):
#     """
#     Add new item to library system
#     :param libsys: LibrarySystem object
#     :param item_type: class, subclass of Item, e.g. Book, DVD, Journal
#     :param name: string, name of item
#     """
#     libsys.load_new_item(item_type, name)
#
#
# def borrow_item(libsys, username, user_id, item_name, item_id, date = datetime.date.today()):
#     """
#     Have user borrow item on date in libsys
#     :param libsys: LibrarySystem object
#     :param username: string, name of user
#     :param user_id: int, unique user id
#     :param item_name: string, name of item
#     :param item_id: int, unique item id
#     :param date: datetime object, date at which item is(/was) borrowed
#     """
#     libsys.borrow_item(username, user_id, item_name, item_id, date)
#
#
# def return_item(libsys, username, user_id, item_name, item_id, date = datetime.date.today()):
#     """
#     Have user return item on date in libsys
#     :param libsys: LibrarySystem object
#     :param username: string, name of user
#     :param user_id: int, unique user id
#     :param item_name: string, name of item
#     :param item_id: int, unique item id
#     :param date: datetime object, date at which item is(/was) borrowed
#     """
#     libsys.return_item(username, user_id, item_name, item_id, date)
