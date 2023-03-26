"""
NAME
    library - implementation of LibraryController class
FILE
    library.py
CLASSES
    LibraryController
    CannotBorrowException: not implemented
"""

import item_list
import user_list
import lib_exceptions


class LibraryController:
    """
    LibraryController class manages users, items, and their interactions.

    Methods defined here:

        user_checkout(...)
            Enables user to check out an item

        user_return(...)
            Enables user to return an item

        user_fine(...)
            Determine fine owed by user

        pay_fine(...)
            Pay money into user's balance of fines

        is_on_loan(...)
            Query checkout status of an item

        add_item(...)
            Add a new library item

        add_user(...)
            Add a new library user
    ----------------------------------------------------------------------
    Attributes defined here:
        max_loans:
            Maximum number if items allowed on loan per user.

        max_fine:
            Maximum amount of accrued fine per user.
    """

    # class attributes
    max_loans = 5     # maximum number of loans
    max_fine = 50.0   # maximum fine (pounds)

    def __init__(self):
        self.item_list = item_list.ItemList()
        self.user_list = user_list.UserList()

    def __del__(self):
        # tidy up our storage
        self.item_list = None
        self.user_list = None

    def user_checkout(self, user_id, item_title, date=False):
        """
        Enables user to check out an item.

        Delegate determining permission and checkout to user list.

        :param user_id: unique ID of user wishing to check out item
        :param item_title: title of item user wishes to check out
        :param date: optional, if provided then used, otherwise set to now
        :return: no return
        """

        # check user object corresponding to given user_id
        if not self.user_list.able_to_borrow(user_id, LibraryController.max_loans, LibraryController.max_fine):
            raise lib_exceptions.CannotBorrowException()

        # get requested item from item_list
        item_requested = self.item_list.get_item(item_title)

        # add item to user's list
        self.user_list.checkout_item(user_id, item_requested, date)

    def user_return(self, user_id, item_id):
        """
        Enables user to return an item.

        Delegate return to user list.
        :param user_id: unique ID of user wishing to return item
        :param item_id: unique ID of item user wishes to return
        :return: no return
        """
        self.user_list.return_item(user_id, item_id)

    def user_fine(self, user_id):
        """
        Determine fine owed by user.

        Delegate fine accrual to user list.
        :param user_id:  unique ID of user
        :return: total fine owed by user
        :rtype: float
        """
        fine = self.user_list.get_fine_total(user_id)
        return fine

    def pay_fine(self, user_id, amount):
        """
        Pay money into user's balance of fines.

        User is allowed to credit their account.
        Delegate payment to user list.
        :param user_id: unique ID of user
        :param amount: user's contribution to their fine account
        :return: no return
        """
        self.user_list.pay_fine(user_id, amount)

    def is_on_loan(self, item_title):
        """
        Query checkout status of an item.

        Delegate query to user list.
        :param item_title: title of item queried
        :return: True if item is on loan, False otherwise
        """

        return self.item_list.is_on_loan(item_title)

    def add_item(self, item_to_add):
        """
        Add a new library item.

        :param item_to_add: Item object to be added to item_list
        :return: no return
        """

        self.item_list.add_item(item_to_add)

    def add_user(self, user_to_add):
        """
        Add a new library user.

        :param user_to_add: User object to be added to user_list
        :return: no return
        """
        self.user_list.add_user(user_to_add)
