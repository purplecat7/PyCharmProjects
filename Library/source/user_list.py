import datetime as dt
from user import User

class UserList():
    """
    A Class to interact between the library interface and available
    user in memory.
    """


    def __init__(self):
        """

        """
        # set up empty list to add all the user classes to.
        self.available_users = []

    def add_user(self, user_to_add):
        """
        A method to add the input user to the self.user_list
        :param user_to_add:
        :return:
        """
        # some code here that appends the current user to
        # the self.available_users on initialisation.

        self.available_users.append(user_to_add)

    def can_borrow(self, user_name, item_name):
        """

        :param user_name: the name of the person
        :param item_name: the name of the item the person
                          wants to borrow.
        :return: a message to the library system to allow
                 borrowing.
        """

        # some code that delegates the user to Carls code.

        # first link to _find_user
        user_to_pass = self._find_user(user_name)

        # second pass all the usefull items to the User handler.
        # Karls_function(user_to_pass)

        User.can_borrow(user_to_pass, item_name)
  

    def checkout_item(self, user_id,matching_item, checkout_date):
        """
        A method to add the new item to a users list of taken out
        items, using Carls code.
        :param matching_item: an item object to add to a users list
        """
        # some code to pass an item object to the user so it can be 
        # added to the users list of borrowed items.

        user_to_act_on = self._find_user(user_id)

        # now add the new item to the person
        user_to_act_on.checkout_item(matching_item, checkout_date)


    def checkin_item(self, user_id, item_obj):
        """
        A method to deal with when a user brings back an item.
        This will tell the user to remove the item from the
        users list of objects.
        :item_obj: an object for the item to add to the user object
        """

        # first find the user fro the list
        user_to_act_on = self._find_user(user_id)

        # then tell the user to checkin the item to the user
        # using Carls Code
        user_to_act_on.check_in(item_obj)

    def _find_user(self, user_id):
        """
        A function to return the class of the person.
        :param user_name: the user_name of the person calling
                          the borrower.
        :return: a class of the person.
        """
        # loops through all the users in self.user_list
        # and returns the class of the desired person.
        #TODO if there are two users with identical identifiers
        # the the last one will be returned - write in an exception
        # to give a proper error.

        for possible_user in self.availble_users:
            # each user has an attribute that is a user id
            # and if it is the right one - return it
            
            if type(user_id) == int:
                if possible_user.user_id == user_id:
                    ret_val = possible_user
            if type(user_id) == str:
                if possible_user.name == user_id:
                    ret_val = possible_user

        return ret_val


