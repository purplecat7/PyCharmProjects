__author__ = 'rsmith31'

import Item


class ItemManager:
    """
    Class that handles the creation of new items
    """

    def __init__(self):
        self.library_controller = None

    def __del__(self):
        pass

    def set_library_controller(self, library_controller):
        self.library_controller = library_controller

    def create_book(self, title, ident):
        """
        Creates a new 'book' object that will be given to the library controller to add to the item list

        :param title: title of the book to be created
        :param ident: id of the book to be created
        :return new_book: the book object that has been created
        """

        new_book = Item.Book(title, ident)

        self.library_controller.additem(new_book)


