"""
NAME
    user_list - implementation of ItemList class
FILE
    user_list.py
CLASSES
    UserList
"""

class UserList(object):
    """
    Class to contain and manage Users, uses dict class to implement storage

    Methods defined here:

        add_user(...)
            Store user object

        able_to_borrow(...)
            Determine whether a user is allowed to borrow another item

        checkout_item(...)
            Assign item to user

        return_item(...)
            Remove item from user

        get_fines(...)
            Returns the accumulated fine from each overdue item.

        pay_fine(...)
            Pay money into user's balance of fines

        checkout_item(...)
            Adds an item being checked out to the item list

        return_item(...)
            Removes an item being checked in from the item list

        get_fine_total(...)
            Calculate total fine owing

    ----------------------------------------------------------------------
    No data or other attributes defined here.

    """
    def __init__(self):

    def __del__(self):
        # tidy up our storage

    def add_user(self, new_user):
        """
        Store user object.

        :param new_user: user object
        :return: no return
        """
        # user stored in dictionary with its id as key.


    def able_to_borrow(self, user_id, max_loans, max_fine):
        """
        Determine whether a user is allowed to borrow another item.

        Delegate to user.
        :param user_id: identifier for user
        :param max_loans: loan limit number as determined by library
        :param max_fine: fine limit amount, as determined by library
        :return: True if user may borrow an item, False otherwise
        :rtype: bool
        """


    def checkout_item(self, user_id, item_requested, date=False):
        """
        Assign item to user.

        Delegate to user.
        :param user_id: user unique identifier
        :param item_requested: unique identifier of item, may be its title or id
        :param date: optional, if provided then used, otherwise set to now
        :return: no return
        """


    def return_item(self, user_id, item_id):
        """
        Remove item from user.

        Delegate to user.
        :param user_id: user unique identifier
        :param item_id: item unique identifier
        :return:
        """


    def get_fine_total(self, user_id):
        """
        Calculate total fine owing.

        Delegate to user.
        :param user_id:
        :return:
        """

    def pay_fine(self, user_id, amount):
        """
        Pay money into user's balance of fines.

        User is allowed to credit their account.
        :param user_id: unique ID of user
        :param amount: user's contribution to their fine account
        :return: no return
        """

    def _find_user(self, user_id):
        # get user object from storage based on unique id
        # return: user object


