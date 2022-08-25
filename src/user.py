"""
File contains the user class for the alexandria library
"""
from item_list import ItemList

class User:
    """
    Class containing attributes and methods for the user.
    Attributes: - user_ID, unique user ID
                - pot, accumulative fine pot for the user
                - myitems, ItemList unique to the user
    Methods: - find_item
             - total_fines, total_borrowed, total_overdue
             - list_borrowed, list_overdue
             - add_to_fine_pot, subtract_from_fine_pot
             - ok_to_checkout, checkout_item
    """

    # class attributes
    def __init__(self, user_ID : int): #constructor
        """
        Attibutes of the class
        """
        # initialise instance attributes
        self.user_ID = user_ID
        self.pot = 0
        self.myitems = ItemList()

    # METHODS

    # find an item from item_list
    def find_item(self, item_title : str):
        """
        Find an item on the user's item-list
        Inputs:
        - self, class
        - item_title, title of item (book, dvd or journal)
        Output: object of the item
        """
        return self.myitems.find_item(item_title)

    # collect total fines from item_list
    def total_fines(self):
        """
        Collect the total fines of the user from the user's item-list
        Inputs:
        - self, class
        Output: total of all user fines
        """
        #find total fines from user's item list
        return self.myitems.check_all_fines(self.user_ID)

    # collect total number of items borrowed from item_list
    def total_borrowed(self): #TODO check with ITEM LIST
        """
        Collect the total number of borrowed items from the user's item-list
        Inputs:
        - self, class
        Output:
        - total number of items borrowed
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
        return self.myitems.check_overdue(self.user_ID)

    # collect list of items borrowed from item_list
    def list_borrowed(self): #TODO check with ITEM LIST
        """
        Collect the list of borrowed items from the user's item-list
        Inputs:
        - self, class
        Output: list of borrowed items
        """
        pass

    # collect list of items borrowed from item_list
    def list_overdue(self): #TODO check with ITEM LIST
        """
        Collect the list of overdue items from the user's item-list
        Inputs:
        - self, class
        Output: list of overdue items
        """
        pass

    # adding fines to the accumulative pot after item is removed from item list
    def add_to_fine_pot(self, amount):
        """
        Add fines to the accumulative pot of fines for the user
        Inputs: self, class
        - amount, fine to add to fine pot
        """
        self.pot +=amount
        pass

    # subtracting fines from the accumulative pot
    def subtract_from_fine_pot(self, amount):
        """
        Subtract fines from the accumulative pot of fines for the user
        Inputs: - self, class
                - amount, fine to add to fine pot
        """
        self.pot -= amount
        pass

    # ask item_list to remove item is this for a returned item?
    def remove_item(self, item_title):   #TODO check with ITEM LIST
        """
        Remove an item from the user's item-list
        Inputs:
        - self, class
        - item_title, title of item (book, dvd or journal)
        """
        # add fines to pot
        #' get fine for the particular item
        # remove from item_list
        self.myitems.remove_item(self, self.user_ID,item_title) #check vitor function
        pass

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
        fines = self.total_fines(self)

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
        # get amount overdue from item_list
        borrowed_total = self.total_borrowed()
        # compare with max_borrowed
        # return true if below, false if not
        if borrowed_total < max_borrowed:
            return True
        else:
            return False


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
        overdue_total = self.total_overdue()
        # compare with max_overdue
        # return true if below, false if not
        if overdue_total <= max_overdue:
            return True
        else:
            return False

    # ok to checkout
    def ok_to_checkout(self, max_fines, max_borrowed, max_overdue):
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
        if self.check_fines(self, max_fines) == True and self.check_overdue(self, max_overdue) == True \
                and self.check_borrowed(self, max_borrowed) == True:
            return True
        else:
            return False

    # checkout an item
    def checkout_item(self, item_title, date):
        """
        Checkout an item from the library and add to the user's item-list
        Inputs:
        - self, class
        - item_title, title of item (book, dvd or journal) : str
        -
        """
        # give item_list title of item
        # item_list should add item to the item_list
        ItemList.add_user_list(self, item_title, date) #TODO vitor add date
        pass




