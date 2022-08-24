"""
Used to initialise the library with a list of items (books, DVDs, journals)
"""
from src.library import Library
from src.item_list import ItemList


class ItemBuilder:

    def __init__(self, file_path):
        self.file_path = file_path
        self.library = None
        self.item_list = ItemList()

    def set_library(self, library):
        """
        Set the library on which we will want to append the built item list
        :param library: Target library object
        """
        self.library = library

    def load_file(self):
        """
        Loads and creates a list of items the contents of file path given
        :return:
        """
        # file to read is self.file_path
        # call self.create(book) for each title
        return self.file_data

    def create_book(self, item_data):
        """
        Creates an book from data given, and appends to the library
        :param item_data: A row or dict of information used to create an item
        """
        # Use NumID.new_id() on book
        # create book using title 'item_data' and id
        # append to self.item_list
        pass

    def create_dvd(self, item_data):
        """
        Creates an dvd from data given, and appends to the library
        :param item_data: A row or dict of information used to create an item
        """
        # Use NumID.new_id() on dvd
        # create dvd using title 'item_data' and id
        # append to self.item_list
        pass

    def create_journal(self, item_data):
        """
        Creates an journal from data given, and appends to the library
        :param item_data: A row or dict of information used to create an item
        """
        # Use NumID.new_id() on journal
        # create journal using title 'item_data' and id
        # append to self.item_list
        pass

    def populate_library(self):
        """
        Sets the item list of the library with the ItemList() generated
        """
        # self.library.add_items(self.item_list)
        pass
