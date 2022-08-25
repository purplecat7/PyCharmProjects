"""
Used to initialise the library with a list of items (books, DVDs, journals)
"""
from src.item_list import ItemList
from src.item_children import Book, DVD, Journal
from src.numbid import NumbID


class ItemBuilder:

    def __init__(self):
        self.file_data = None
        self.library = None
        self.item_list = ItemList()

    def set_library(self, library):
        """
        Set the library on which we will want to append the built item list
        :param library: Target library object
        """
        self.library = library

    def load_books_in_file(self, file_path):
        """
        Loads and creates a list of items the contents of file path given
        :return: Optional - Returns the full file contents - a title list - if desired
        """
        with open(file_path) as f:
            file_data = f.readlines()

        for title in file_data:
            self.create_book(title)

        return file_data  # Optional return

    def create_book(self, title):
        """
        Creates an book from data given, and appends to the library
        :param title: A string
        """
        self.item_list.add_item(Book(NumbID.new_id(), title))
        pass

    def create_dvd(self, title):
        """
        Creates an dvd from data given, and appends to the library
        :param title: A string
        """
        self.item_list.add_item(DVD(NumbID.new_id(), title))

    def create_journal(self, title):
        """
        Creates an journal from data given, and appends to the library
        :param title: A string
        """
        self.item_list.add_item(Journal(NumbID.new_id*(), title))

    def populate_library(self):
        """
        Sets the item list of the library with the ItemList() generated
        """
        self.library.add_items(self.item_list)
        NumbID.reset_id()