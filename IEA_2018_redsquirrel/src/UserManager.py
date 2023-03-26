"""
NAME
    user_manager - implementation of ItemManager class
FILE
    user_manager.py
CLASSES
    UserManager
"""

from User import User


class UserManager(object):
    """
    Class handling the creation of new users

    Methods defined here:

        set_library_controller(...)
            Store a reference to the LibraryController object

        create_user(...)
            Create a new 'user' object and pass to the library controller to add to its item list

    ----------------------------------------------------------------------
    No data or other attributes defined here.

    """

    def __init__(self,lib_controller):
        self._library_controller = lib_controller

    def __del__(self):
        pass


    def create_user(self, user_id):
        """
        Create a new 'user' object and pass to the library controller to add to its user list

        :param user_id: unique identifier for the user
        :return: no return
        """

        # create user with user id
        my_user = User(user_id)

        # pass user to lib controller
        self._library_controller.add_user(my_user)
