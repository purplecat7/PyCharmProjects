"""
A class that describes the user list.

Has methods to:


"""

from user import User


class UserList:
    """
    This class is a list of all the users in the library system.

    It has methods to:
        Add a new user to the list.
        Find a user on the list from its ID

    """

    def __init__(self):
        # create a list
        self.userlist = list()


    def __del__(self):
        pass

    def add_user(self, user):
        """
        Add a new user item to the list
        :param user:
        :return:
        """
        #add the user to the list
        self.userlist.append(user)

    def find(self, id):
        """
        Find the user from the ID on the list
        :param id:
        :return: the item with that ID
        """
        #for each item in the list check its ID
        # and return the user whose ID matches the ID provided or None if user doesn't exist
        for user in self.userlist:
            if id == user.get_id():
                return user
        else:
            return False

    def able_to_borrow(self, id, maxfines, maxallowed):
        """
        Find if a user is able to borrow a new item.
        :param id:
        :return: bool
        """
        #Find the Item on the list from the ID
        user = self.find(id)
        #check its a valid id throw exception if not
        #ask the user if it can borrow
        return user.able_to_borrow(maxfines, maxallowed)

    def checkout(self, id, item):
        """
        Checkout the book to a user on the list.
        :param id:
        :param item:
        :return: calls checkout on the user with item
        """
        #Find the user on the list
        user = self.find(id)
        #tell user to checkout item
        return user.checkout(item)

    def return_item(self, id, item):
        """
        Return the an item in a users account.
        :param id:
        :param Item:
        :return: returns item that user (with id) has out.
        """
        #Find the user in the list
        user = self.find(id)
        #Tell user to return the item.
        return user.return_item(item)