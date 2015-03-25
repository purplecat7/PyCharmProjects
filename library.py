"""
Definition of LibraryController class.

Author: SimonPeatman"""
__author__ = 'SimonPeatman'


class LibraryController:
    """
    LibraryController class for LibrarySystem.

    Saves lists of items and users; handles checking out of items."""

    # parameters
    max_loans = 5     # maximum number of loans
    max_fine = 50.0   # maximum fine (pounds)

    def __init__(self, item_list, user_list):
        """
        Constructor method of LibraryController class.

        :param item_list: list of Item objects
        :param user_list: list of User objects"""

        self.item_list = item_list
        self.user_list = user_list

    def user_checkout(self, user_id, item_title):
        """
        Handles checking out of an item by a user.

        :param user_id: unique ID of user wishing to check out item
        :param item_title: title of item user wishes to check out"""

        # get user object corresponding to given user_id
        user = self.user_list.lookup_details(user_id)

        # check whether user is allowed to borrow item
        if not user.is_it_ok_to_borrow(LibraryController.max_loans, LibraryController.max_fine):
            raise CannotBorrowException()

        # get requested item from item_list
        item_requested = self.item_list.find_item(item_title)

        # add item to user's list
        user.add_item(item_requested)


class CannotBorrowException(Exception):
    pass
