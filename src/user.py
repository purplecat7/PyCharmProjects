"""
File contains the user class for the alexandria library
"""

class UserClass:

    # class attributes
    def __init__(self): #constructor
        """
        Attibutes of the class
        """
        # initialise instance attributes
        # ID, name
        self.__user_ID : str
        self.__user_name : str


    # class methods

    # find an item from item_list
    def find_item(self, item_title):
        """
        Find an item on the user's item-list
        Inputs:
        - self, class
        - item_title, title of item (book, dvd or journal)
        Output: object of the item
        """
        pass
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
    def add_to_fine_pot(self, ):
        # need to know we've
    # ask item_list to remove item
    def remove_item(self, item_title):

    # subtracting fines from the accumulative pot
    # check pot amount against given amount from library
    # check pot plus fine amount against given amount from library
    # check borrowed amount against given amount from library
    # check overdue amount against given amount from library


