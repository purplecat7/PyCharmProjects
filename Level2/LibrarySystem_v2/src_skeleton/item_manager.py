"""
NAME
    item_manager - implementation of ItemManager class
FILE
    item_manager.py
CLASSES
    ItemManager
"""

import item


class ItemManager:
    """
    Class handling the creation of new items

    Methods defined here:

        set_library_controller(...)
            Store a reference to the LibraryController object

        create_book(...)
            Create a new 'book' object and pass to the library controller to add to its item list

        create_dvd(...)
            Create a new 'dvd' object and pass to the library controller to add to its item list

        create_journal(...)
            Create a new 'journal' object and pass to the library controller to add to its item list

    ----------------------------------------------------------------------
    No data or other attributes defined here.

    """

    def __init__(self):


    def __del__(self):
        pass

    def set_library_controller(self, library_controller):
        """
        Store a reference to the LibraryController object

        :param library_controller: the LibraryController object
        :return: no return
        """

    def create_book(self, title, ident):
        """
        Create a new 'book' object and pass to the library controller to add to its item list

        :param title: title of the book to be created
        :param ident: id of the book to be created
        :return: no return
        """

    def create_dvd(self, title, ident):
        """
        Create a new 'dvd' object and pass to the library controller to add to its item list

        :param title: title of the dvd to be created
        :param ident: id of the dvd to be created
        :return: no return
        """

    def create_journal(self, title, ident):
        """
        Create a new 'journal' object and pass to the library controller to add to its item list

        :param title: title of the journal to be created
        :param ident: id of the journal to be created
        :return: no return
        """



