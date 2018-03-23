import datetime

try:
    from .Item import Item
except ImportError:
    class Item:
        def __init__(self, title, identity, checkout_date):
            self._identity = identity
            self._title = title
            self._checkout_date = checkout_date

        def get_identifier(self):
            return self._identity


class ItemNotFound(Exception):
    """
    Exception class for items not found in the library collection
    """
    pass


class ItemNotUnique(Exception):
    """
    Exception class for finding too many items for title lookup
    """
    pass


class ItemCollection:
    def __init__(self):
        """
        A collection of items held by the library. Data held in a dictionary
        indexed by the item ID.
        """
        self._items = {}

    def __del__(self):
        """
        Remove the items on deletion
        """
        del self._items

    @staticmethod
    def _item_not_found():
        """
        Helper method to do something is we can't find an item
        :raise:
        """
        raise ItemNotFound("Item not found in item collection")

    @staticmethod
    def _get_key(item):
        """
        Get the key (id) of the item. If we are given a int assume that is
        the id if not assume we have been given an item and use the
        item.get_identifier method

        :param item: The item id (int) or an item object
        :return: The item id
        """
        if type(item) is int:
            return item
        else:
            return item.get_identifier(None)

    def add_item(self, item):
        """
        Add an item to the collection

        :param item: The item to add
        """
        self._items[item.get_identifier(None)] = item

    def remove_item(self, item):
        """
        Remove an item from the collection

        :param item: The item id (int) or an item object
        :raise: ItemNotFound if the item is not found
        """
        key = self._get_key(item)

        try:
            del self._items[key]
        except KeyError:
            self._item_not_found()

    @staticmethod
    def _fuzz(title):
        """
        Fuzz the title string, lower the case and remove the non alpha numeric
        characters
        :param title: Title str
        :return: Title str fuzzed
        """
        return ''.join(filter(str.isalnum, title)).lower()

    def search_for_title(self, title):
        """
        Search for items with a title string
        :param title: Title string to search for
        :return: A list of items that match the title
        """
        items = []
        for ids, item in self._items.items():
            if self._fuzz(title) in self._fuzz(item.get_title()):
                items.append(item)
        return items

    def get_item(self, item_key):
        """
        Get item by id (if int) or title (if string)
        :param item_key: The id as an int or the title as a string
        :return: The item object
        """
        if type(item_key) == str:
            return self.get_item_by_title(item_key)
        elif type(item_key) == int:
            return self.get_item_by_id(item_key)
        elif type(item_key) == Item:
            return item_key
        else:
            raise TypeError

    def get_item_by_title(self, title):
        """
        Get the item by title
        :param title: The title to get the item by
        :return: The item object
        """
        items = self.search_for_title(title)
        if len(items) == 0:
            self._item_not_found()
        elif len(items) > 1:
            raise ItemNotUnique('Found two or more items by title: {}'.format(
                [i.get_title() for i in items]
                ))
        else:
            return items[0]

    def get_item_by_id(self, item_id):
        """
        Get an item. by id Return the item object
        :param item_id: The id or the item
        :return: item
        :raises: ItemNotFound if the item is not found
        """
        try:
            return self._items[item_id]
        except KeyError:
            self._item_not_found()

    @property
    def number_of_items(self):
        """
        Return the number of items
        :return: Number of items in the collection
        """
        return len(self._items)

    def is_on_loan(self, item):
        """
        Return if the item is on loan

        :param item: The id or the item
        :return: Output of item.is_checked_out
        :raises: ItemNotFound if the item is not found
        """
        key = self._get_key(item)

        try:
            return self._items[key].is_checked_out()
        except KeyError:
            self._item_not_found()

    def return_item(self, item):
        """
        Return the item

        :param item: The id or the item
        :return: The fine due on return
        :raises: ItemNotFound if the item is not found
        """
        key = self._get_key(item)

        try:
            fine = self._items[key].get_fine_due()
            self._items[key].reset_checkout()
            return fine
        except KeyError:
            self._item_not_found()

    def checkout_item(self, item, date=None):
        """
        Checkout an item

        :param date: The date the item was checkout
        :param item: The id or the item
        :return: Output of item.set_checkout
        :raises: ItemNotFound if the item is not found
        """
        key = self._get_key(item)

        if date is None:
            date = datetime.datetime.now()

        try:
            return self._items[key].set_checkout(date)
        except KeyError:
            self._item_not_found()

    def get_fines(self):
        """
        Get all the fines for the items in the collection
        :return: The totel fine
        """
        fine = 0.0
        for ids, item in self._items.items():
            fine = fine + item.get_fine_due()
        return fine
