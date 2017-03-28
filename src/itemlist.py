__author__ = 'nerc'
from datetime import datetime

class ItemList(list):

    def __init__(self):
        # initialise attributes
        pass

    def __del__(self):
        pass

    def add_item(self, new_item):
        """

        :param new_item:
        :return:
        """
        self.append(new_item)

    def checkout_item(self, item):
        """
        Finds the requested item and changes the check out date to
        today's date.
        :param item:
        :return:
        """
        to_checkout = self.get_item(item)
        to_checkout.set_checkout(datetime.now())

    def get_fines(self, item):
        """
        Returns the fines on the item.
        :return:
        """
        fined_item = self.get_item(item)
        fined_item.get_fine_due()

    def get_item(self, item):
        """
        Finds the requested item
        :param item: the requested item
        :return:
        """
        return next((x for x in self if x.identity == item), None)

    def is_on_loan(self, item):
        """
        Checks if an item is checked out.
        :return:
        """
        loan_item = self.get_item(item)
        loan_item.is_checked_out()

    def number_of_items(self):
        """
        Returns the number of items in item list
        :return:
        """
        return len(self)

    def remove_item(self, item):
        """
        Removes an item from the item list
        :param item: Item to be removed
        :return:
        """
        remove_item = self.get_item(item)
        self.remove(remove_item)

    def return_item(self, item):
        """

        :return:
        """
        returning = self.get_item(item)
        returning.reset_checkout()

