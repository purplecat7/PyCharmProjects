__author__ = 'nerc'
from datetime import datetime


class ItemList(list):

    def __init__(self):
        super.__init__()
        # initialise attributes
        pass

    def __del__(self):
        pass

    def add_item(self, new_item):
        """
        Adds an item object
        :param new_item: item to be added to item list
        :return:
        """
        self.append(new_item)

    def checkout_item(self, item_id):
        """
        Finds the requested item and changes the check out date to
        today's date.
        :param item_id: ID of item to be checked out
        :return:
        """
        to_checkout = self.get_item(item_id)
        to_checkout.set_checkout(datetime.now())

    def get_fines(self, item_id):
        """
        Finds the item from its ID and returns the fines incurred on item.
        :param item_id: ID of item to be returned
        :return:
        """
        fined_item = self.get_item(item_id)
        fined_item.get_fine_due()

    def get_item(self, ID):
        """
        Finds the requested item from its ID, which can be either
        an integer or a string
        :param ID: the requested item
        :return:
        """
        if type(ID) is int:
            identifier_type = 'ID'
        elif type(ID) is str:
            identifier_type = 'Title'
        else:
            print "ID is neither integer nor string."

        for item in self:
            if ID == item.get_identifier(identifier_type):
                return item

    def is_on_loan(self, item_id):
        """
        Finds item from ID and checks if item is on loan
        :param item_id: ID of item to be removed
        :return:
        """
        loan_item = self.get_item(item_id)
        loan_item.is_checked_out()

    def number_of_items(self):
        """
        Returns the number of items in item list
        :return:
        """
        return len(self)

    def remove_item(self, item_id):
        """
        Finds item and removes an item from the item list
        :param item_id: ID of item to be removed
        :return:
        """
        remove_item = self.get_item(item_id)
        self.remove(remove_item)

    def return_item(self, item_id):
        """
        Finds an item from its ID and sets its checkout date to 'None'
        :param item_id: ID of item to be returned
        :return:
        """
        returning = self.get_item(item_id)
        returning.reset_checkout()

