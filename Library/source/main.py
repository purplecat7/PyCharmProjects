from libsys import LibrarySystem
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



def setup_libsys(filename = False):

    libsys = LibrarySystem()
    # instantiate Library System

    if filename:

        libsys.load_items(filename)
        # load items from specified file to the Library System


def add_new_item(libsys, item_type, name):

    libsys.load_new_item(item_type, name)


def borrow_item(libsys, username, user_id, item_name, item_id, date = datetime.date.today()):

    libsys.borrow_item(username, user_id, item_name, item_id, date)


def scenario1(libsys):

    borrow_item(libsys, "JohnnyCodewarrior", None, "Document, Your job depends on it", None)


def return_item(libsys, username, user_id, item_name, item_id, date = datetime.date.today()):

    libsys.return_item(username, user_id, item_name, item_id, date)


def scenario2(libsys, overdueJournalName):

    return_item(libsys, "JudyHacker", None, overdueJournalName, None)
    borrow_item(libsys, "JudyHacker", None, "Debugging to music", None)


def scenario3(libsys):



