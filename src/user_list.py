"""
A class that describes the user list.


"""

class UserList:
    """
    This class is a list of all the users in the library system.

    It has methods to:
        Add a new user to the list.
        Find a user on the list from its ID

    """

    def __init__(self):
        # create a list


    def __del__(self):
        pass

    def add_user(self, user):
        """
        Add a new user item to the list
        :param user:
        :return:
        """
        #add the user to the list

    def find(self,ID):
        """
        Find the user from the ID on the list
        :param ID:
        :return: the item with that ID
        """
        #for each item in the list check its ID
        # and return the user whose ID matches the ID provided or None if user doesn't exist

    def able_to_borrow(self, ID):
        """
        Find if a user is able to borrow a new item.
        :param ID:
        :return: bool
        """
        #Find the Item on the list from the ID
        #if user not on list return false
        #ask the user if it can borrow

    def checkout(self, ID,  item):
        """
        Checkout the book to a user on the list.
        :param ID:
        :param item:
        :return:
        """
        #Find the user on the list
        #tell user to checkout item

    def return_item(self, ID, Item):
        """
        Return the an item in a users account.
        :param ID:
        :param Item:
        :return:
        """
        #Find the user in the list
        #Tell user to return the item.