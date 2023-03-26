from item import Book, DVD, Journal
from library_system import LibrarySystem


class ItemInitialise:

    def __init__(self, library_system):
        from main import NumbID
        self.libsys = library_system
        self.IDgen = NumbID()


    def __del__(self):

        pass


    def load_items(self, filename, item_type):
        """
        Takes list of files and their type and adds to library_system itemlist
        :param filename: string, name of file of names of items
        :param item_type: class, subclass of Item, type of item in file
        """
        file = open(filename, 'r')
        for item_name in file.readlines():
        # iterate over names of items in file
            item_name = item_name[:-1]
            #TODO Ugly fix to remove the '/n' from the end of lines
            new_item = item_type(item_name, self.IDgen.new_id())
            # create object of class item_type for each name, assigning a unique id number & name
            self.libsys.add_new_item(new_item)
            # tell libsys to add object to itemlist
        file.close()


    def load_new_item(self, item_name, item_type):
        """
        Creates single item of specified type and adds to list
        :param itemlist: ItemList object to add items to
        :param item_name: string, name of item
        :param item_type: class, subclass of Item, type of item in file
        """

        new_item = item_type(item_name, self.IDgen.new_id())
        # create object of class item_type, assigning a unique id number & name

        self.libsys.add_new_item(new_item)
        # tell libsys to add object to given itemlist

