__author__ = 'rsmith31'

import item


class ItemManager:
    """
    Class that handles the creation of new items
    """

    def __init__(self):
        self.library_controller = None

    def __del__(self):
        pass

    def set_library_controller(self, library_controller):
        """
        Setter method for the library_controller that will deal with new items

        :param library_controller: the library_controller object that will be set
        :return none:
        """
        self.library_controller = library_controller

    def create_book(self, title, ident):
        """
        Creates a new 'book' object that will be given to the library controller to add to the item list

        :param title: title of the book to be created
        :param ident: id of the book to be created
        :return none:
        """

        new_book = item.Book(title, ident)

        self.library_controller.add_item(new_book)


