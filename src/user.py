"""
File contains the user class for the alexandria library
"""
from item_list import ItemList
# TODO need to import the library to know what the max fines etc are? or will this info be passed to the user

class UserClass:

    # class attributes
    def __init__(self, user_ID): #constructor
        """
        Attibutes of the class
        """
        # initialise instance attributes
        # ID, name
        self.user_ID = user_ID
        self.pot = 0
        #self.user_name = None

    # METHODS

    # find an item from item_list
    def find_item(self, item_title):
        """
        Find an item on the user's item-list
        Inputs:
        - self, class
        - item_title, title of item (book, dvd or journal)
        Output: object of the item
        """
        # find an item in the user's item_list
        item = ItemList.item_title # not the case
        return item

    # collect total fines from item_list
    def total_fines(self):
        """
        Collect the total fines of the user from the user's item-list
        Inputs:
        - self, class
        Output:
        - total of all fines
        """
        pass

    # collect total number of items borrowed from item_list
    def total_borrowed(self):
        """
        Collect the total number of borrowed items from the user's item-list
        Inputs:
        - self, class
        Output:
        - total number of items borrowed
        """
        pass

    # collect list of items borrowed from item_list
    def list_borrowed(self):
        """
        Collect the list of borrowed items from the user's item-list
        Inputs:
        - self, class
        Output:
        - list of borrowed items
        """
        pass

    # collect total number of items overdue from item_list
    def total_overdue(self):
        """
        Collect the total number of overdue items from the user's item-list
        Inputs:
        - self, class
        Output:
        - total number of items overdue
        """
        pass

    # collect list of items borrowed from item_list
    def list_overdue(self):
        """
        Collect the list of overdue items from the user's item-list
        Inputs:
        - self, class
        Output:
        - list of overdue items
        """
        pass

    # adding fines to the accumulative pot after item is removed from item list
    def add_to_fine_pot(self, amount):
        """
        Add fines to the accumulative pot of fines for the user
        """
        # TODO: need to know we've removed the item??

    # ask item_list to remove item is this for a returned item?
    def remove_item(self, item_title):
        """
        Remove an item from the user's item-list
        Inputs:
        - self, class
        - item_title, title of item (book, dvd or journal)
        """
        pass

    # subtracting fines from the accumulative pot
    def subtract_from_fine_pot(self, amount):
        """
        Add fines to the accumulative pot of fines for the user
        """
        # TODO: need to know we've removed the item??

    # check pot amount against given amount from library, is this necessary?

    # check pot plus fine amount against given amount from library
    def check_fines(self, max_fines):
        """
        Check if the fines are below the maximum fine amount prescribed by the library
        Inputs:
        - self, class
        - max_fines, amount given by library
        Outputs:
        - True, below max amount
        - False, not below
        """
        # get fines from item_list
        fines = UserClass.total_fines(self)

        # get fines from accumulated pot
        pot_fines = self.pot

        # add amounts
        total = fines + pot_fines

        # compare with max_fines
        # return true if below, false if not
        if total < max_fines:
            return True
        else:
            return False

    # check borrowed amount against given amount from library
    def check_borrowed(self, max_borrowed):
        """
        Check if the number of books borrowed is below the maximum amount prescribed by the library
        Inputs:
        - self, class
        - max_borrowed, amount given by library
        Outputs:
        - True, below max amount
        - False, not below
        """
        # get amount borrowed from item_list
        # compare with max_borrowed
        # return true if below, false if not

    # check overdue amount against given amount from library
    def check_overdue(self, max_overdue):
        """
        Check if the number of books overdue is below the maximum amount prescribed by the library
        Inputs:
        - self, class
        - max_overdue, amount given by library
        Outputs:
        - True, below max amount
        - False, not below
        """
        # get amount overdue from item_list
        # compare with max_overdue
        # return true if below, false if not

    # ok to checkout
    def ok_to_checkout(self):
        """
        Check if an account is ok to check out. Check previous functions are true?
        Outputs:
        - True, ok to checkout
        - False, not ok
        """
        # check that all the following are true:
        # check_fines
        # check_borrowed
        # check_overdue
        # return true if ok, false if not

    # checkout an item
    def checkout_item(self, item_title):
        """
        Checkout an item from the library and add to the user's item-list
        Inputs:
        - self, class
        - item_title, title of item (book, dvd or journal)
        """
        # give item_list title of item
        # item_list should add item to the item_list
        pass




