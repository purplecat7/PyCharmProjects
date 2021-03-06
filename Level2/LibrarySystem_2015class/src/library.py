"""
Definition of LibraryController class.

Author: SimonPeatman"""
__author__ = 'SimonPeatman'

import itemList
import userList


class LibraryController:
    """
    LibraryController class for LibrarySystem.

    Saves lists of items and users.
    Handles creation of library items and users, and checking out of items."""

    # parameters
    max_loans = 5     # maximum number of loans
    max_fine = 50.0   # maximum fine (pounds)

    def __init__(self):
        """
        Constructor method of LibraryController class."""

        self.item_list = itemList.ItemList()
        self.user_list = userList.UserList()

    def user_checkout(self, user_id, item_title):
        """
        Handles checking out of an item by a user.

        :param user_id: (int) unique ID of user wishing to check out item
        :param item_title: (str) title of item user wishes to check out"""

        # get user object corresponding to given user_id
        user = self.user_list.find_user(user_id)

        # check whether user is allowed to borrow item
        if not user.able_to_borrow(LibraryController.max_loans, LibraryController.max_fine):
            raise CannotBorrowException()

        # get requested item from item_list
        item_requested = self.item_list.get_item(item_title)

        # add item to user's list
        user.checkout_item(item_requested)

    def user_return(self, user_id, item_id):
        """
        Handles returning item by a user."""

        # get user object corresponding to given user_id
        user = self.user_list.find_user(user_id)
        
        user.return_item(item_id)


    def user_fine(self, user_id):

        # get user object corresponding to given user_id
        user = self.user_list.find_user(user_id)

        fine = user.get_fine_total()
        
        return fine
                

    def add_item(self, item_to_add):
        """
        Add a new library item to self.item_list.

        :param item_to_add: Item object to be added to self.item_list"""

        self.item_list.add_item(item_to_add)

    def add_user(self, user_to_add):
        """
        Add a new library user to self.user_list.

        :param user_to_add: User object to be added to self.user_list"""

        self.user_list.add_user(user_to_add)


class CannotBorrowException(Exception):
    pass
