from user import User
from user_error import UserError

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
        :return: nothing - just adds a new user to my userlist
        """
        # some code here that appends the current user to
        # the self.available_users on initialisation.

        self.available_users.append(user_to_add)

    def can_borrow(self, user_id):
        """

        :param user_name: the name of the person
        :return: a message to the library system to allow
                 borrowing. True/False
        """

        # some code that delegates the user to Carls code.

        # first link to _find_user
        user_to_pass = self._find_user(user_id)

        # then actually find out if it can borrow

        return user_to_pass.can_borrow()
  

    def checkout_item(self, user_id,matching_item, checkout_date = None):
        """
        A method to add the new item to a users list of taken out
        items, using Carls code.
        :param matching_item: an item object to add to a users list
        """
        # some code to pass an item object to the user so it can be 
        # added to the users list of borrowed items.

        user_to_act_on = self._find_user(user_id)

        # now add the new item to the person
        user_to_act_on.checkout(matching_item, checkout_date)


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

        # set a clicker that will show if the user has been found
        found_the_user = False

        for possible_user in self.available_users:
            # each user has an attribute that is a user id
            # and if it is the right one - return it
            
            if type(user_id) == int:
                if possible_user.user_id == user_id:
                    ret_val = possible_user
                    found_the_user = True
            if type(user_id) == str:
                if possible_user.name == user_id:
                    ret_val = possible_user
                    found_the_user = True

        if found_the_user:

            return ret_val

        else:

            raise UserError()



