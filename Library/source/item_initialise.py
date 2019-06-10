from item import Book, DVD, Journal

class ItemInitialise():

    def __init__(self, library_system):

        self.libsys = library_system


    def __del__(self):

        pass


    def load_items(self, itemlist, filename, item_type):
        """
        Takes list of files and their type and adds to library_system itemlist
        :param itemlist: ItemList object to add items to
        :param filename: string, name of file of names of items
        :param item_type: class, subclass of Item, type of item in file
        """

        # iterate over names of items in file

            # create object of class item_type for each name, assigning a unique id number & name

            # tell libsys to add object to given itemlist


    def load_new_item(self, itemlist, item_name, item_type):
        """
        Creates single item of specified type and adds to list
        :param itemlist: ItemList object to add items to
        :param item_name: string, name of item
        :param item_type: class, subclass of Item, type of item in file
        """

        # create object of class item_type, assigning a unique id number & name

        # tell libsys to add object to given itemlist

