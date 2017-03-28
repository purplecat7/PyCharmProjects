__author__ = 'nerc'
from datetime import datetime

class ItemList(list):

    def __init__(self):
        # initialise attributes
        pass

    def __del__(self):
        pass

    def addItem(self, new_item):
        """

        :param new_item:
        :return:
        """
        self.append(new_item)

    def checkout_item(self, item):
        """

        :param item:
        :return:
        """
        to_checkout = next((x for x in self if x._identity == item), None)
        to_checkout.set_checkout(datetime.now())


    def get_fines(self):
        """

        :return:
        """
        pass

    def get_item(self):
        """

        :return:
        """
        pass

    def is_on_loan(self):
        """

        :return:
        """
        pass

    def number_of_items(self):
        """

        :return:
        """
        pass

    def remove_item(self):
        """

        :return:
        """
        pass

    def return_item(self):
        """

        :return:
        """
        pass