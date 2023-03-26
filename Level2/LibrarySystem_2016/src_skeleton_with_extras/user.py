"""
NAME
    user - implementation of User class
FILE
    user.py
CLASSES
    User

"""

import item_list


class User(object):
    """
    Class to create users for the library system

    Methods defined here:
        get_identification(...)
            Get the user's unique id

        set_identification(...)
            Set the user's unique id

        able_to_borrow(...)
            Decide whether or not the user can borrow an item.

        checkout_item(...)
            Loan an item to a user

        return_item(...)
            Return an item to the library

        get_fine_total(...)
            Retrieve total amount of fines owed by user

    ----------------------------------------------------------------------
    No data or other attributes defined here.

    """

    def __init__(self):
        self._identification = int()
        self._fines = float()
        self._user_items = item_list.ItemList()

    def __del__(self):
        # tidy up our storage
        self._user_items = None

    def get_identification(self):
        """
        Get the user's unique id

        :return: unique id
        :rtype: int
        """

    def set_identification(self, value):
        """
        Set the user's unique id

        :param value: id
        :return: no return
        """

    def able_to_borrow(self, max_number_loans, max_total_fine):
        """
        Decide whether or not the user can borrow an item.

        Decision based on whether the maximum number of loanable items is exceeded or
        maximum total fine is exceeded.
        :param max_number_loans:
        :param max_total_fine:
        :return: True if user may borrow another item, False otherwise
        :rtype: bool
        """
        # get the fines currently owed on checked out items, add to our oustanding total
        # get number of items on loan

        # assess whether user can borrow
        too_many_loans = current_loans >= max_number_loans
        too_much_fine = current_fines >= max_total_fine
        if too_many_loans or too_much_fine:
            return False  # cannot borrow
        else:
            return True  # can borrow

    def checkout_item(self, item_requested, date=False):
        """
        Loan an item to a user.
        Delegate item handling to the user's list.

        :param item_requested: Item object
        :param date: optional, if provided then used, otherwise set to now
        :return: no return
        """

    def return_item(self, item_id):
        """
        Return an item to the library.
        Delegate item handling to the user's list, where it is removed.

        :param item_id:
        :return: no return
        """
        # make sure we get any fine due on the item and add to our total

    def get_fine_total(self):
        """
        Retrieve total amount of fines owed by user.
        Delegate item handling to the user's list, where each item may be queried.
        Add to accumulated fine for returned items.

        :return: total fine owed by user
        :rtype: float
        """

    def pay_fine(self, amount):
        """
        Pay money into user's balance of fines.

        User is allowed to credit their account.
        :param amount: user's contribution to their fine account
        :return: no return
        """

