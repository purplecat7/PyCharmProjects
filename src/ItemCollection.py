import datetime

try:
    from Item import Item
except ImportError:
    class Item:
        def __init__(self, title, identity, checkout_date):
            self._identity = identity
            self._title = title
            self._checkout_date = checkout_date

        def get_id(self):
            return self._identity


class ItemNotFound(Exception):
    """
    Exception class for items not found in the library collection
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
        item.get_id method

        :param item: The item id (int) or an item object
        :return: The item id
        """
        if type(item) is int:
            return item
        else:
            return item.get_id

    def add_item(self, item):
        """
        Add an item to the collection

        :param item: The item to add
        """
        self._items[item.get_id] = item

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

    def get_item(self, item_id):
        """
        Get an item. Return the item object
        :param item_id: The id or the item
        :return: item
        :raises: ItemNotFound if the item is not found
        """
        try:
            return self._items[item_id]
        except KeyError:
            self._item_not_found()

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
        :return: Output of item.reset_checkout
        :raises: ItemNotFound if the item is not found
        """
        key = self._get_key(item)

        try:
            return self._items[key].reset_checkout()
        except KeyError:
            self._item_not_found()

    def checkout_item(self, item):
        """
        Checkout an item

        :param item: The id or the item
        :return: Output of item.set_checkout
        :raises: ItemNotFound if the item is not found
        """
        key = self._get_key(item)

        try:
            current_data = datetime.datetime.now()
            return self._items[key].set_checkout(current_data)
        except KeyError:
            self._item_not_found()
