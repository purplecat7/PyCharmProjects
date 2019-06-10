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

        # self.available_users.append(user_to_add)

        pass

    def can_borrow(self, user_name, item_name, passed_date=None):
        """

        :param user_name: the name of the person
        :param item_name: the name of the item the person
                          wants to borrow.
        :return: a message to the library system to allow
                 borrowing.
        """

        # some code that delegates the user to Karls code.

        # first link to _find_user
        # user_to_pass = _find_user(user_name)

        # second pass all the usefull items to the User handler.
        # Karls_function(user_to_pass)
        # if passed_date == None:
        #    passed_date = dt.date.today()
        # User.can_borrow(user_to_pass)
        
        pass
  

    def checkout_item(self, matching_item):
        
        # some code to pass an item object to the user so it can be 
        # added to the users list of borrowed items.
        
        # User.checkout_item(matching_item)
        
        pass
    
    def _find_user(self, user_name):
        """
        A function to return the class of the person.
        :param user_name: the user_name of the person calling
                          the borrower.
        :return: a class of the person.
        """
        # loops through all the users in self.user_list
        # and returns the class of the desired person.

        # for possible_user in self.availble_users:
            # if possible_user meets some requirment that matches
            # it to the user_name:
                # return possible_user
        pass

