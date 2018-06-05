"""
A class that describes the user list.
"""

from user import User


class UserList:
    """
    A class for a list of users.

    Attributes:
        user_list             : list, contains all the user objects


    Methods:
        add_user             : adds a user to the list
        find                 : returns a user from the list given their ID
        able_to_borrow       : return bool specifying whether the user can borrow a new item
        checkout             : passes checkout message to a user on the list
        return_item          : passes return message to a user on the list

    """

    def __init__(self):
        # create a list
        self.user_list = list()

    def __del__(self):
        pass

    def add_user(self, user):
        """
        Add a new user item to the list

        :param user: user object, to be added to the list
        """
        # add the user to the list
        self.user_list.append(user)

    def find(self, user_id):
        """
        Find the user from the ID on the list

        :param user_id: int, id of a user to find on the list
        :return: User object or None if no user with that id is on the list
        """
        # for each item in the list check its ID
        # and return the user whose ID matches the ID provided or None if user doesn't exist
        for user in self.user_list:
            if user_id == user.get_id():
                return user
        else:
            return None

    def able_to_borrow(self, user_id, max_fines, max_allowed):
        """
        Find if a user is able to borrow a new item.

        :param user_id: int, id of a user to find on the list
        :param max_fines: float, max amount of fines allowed
        :param max_allowed: int, max amount of items allowed checked out
        :return: bool specifying whether a user may borrow
        """
        # Find the Item on the list from the ID
        user = self.find(user_id)
        # check its a valid user_id (could throw exception if not)
        # ask the user if it can borrow
        return user.able_to_borrow(max_fines, max_allowed)

    def checkout(self, user_id, item):
        """
        Checkout the book to a user on the list.

        :param user_id: an int giving the id of a user to find on the list
        :param item: an item object for the user to checkout
        :return: calls checkout on the user with item
        """
        # Find the user on the list
        user = self.find(user_id)
        # tell user to checkout item
        return user.checkout(item)

    def return_item(self, user_id, item):
        """
        Return the an item in a users account.

        :param user_id: an int giving the id of a user to find on the list
        :param item: an item object for the user to checkout
        :return: returns item that user (with id) has out.
        """
        # Find the user in the list
        user = self.find(user_id)
        # Tell user to return the item.
        return user.return_item(item)

    def fines_owed(self,user_id):
        # Find the user in the list
        user = self.find(user_id)
        # ToDo Get fines due from user

    def pay_fine(self, user_id, amount):
        # find user
        user = self.find(user_id)
        # TODO have user pay amount
