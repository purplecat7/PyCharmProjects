"""
NAME
    user_manager - implementation of ItemManager class
FILE
    user_manager.py
CLASSES
    UserManager
"""

import user


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

    def __init__(self):
        self._library_controller = None

    def __del__(self):
        pass

    def set_library_controller(self, library_controller):
        """
        Store a reference to the LibraryController object

        :param library_controller: the LibraryController object
        :return: no return
        """

    def create_user(self, user_id):
        """
        Create a new 'user' object and pass to the library controller to add to its user list

        :param user_id: unique identifier for the user
        :return: no return
        """
        # create user object and set its id
        # tell the library controller about it


class UserManager:
    # Q: What is a "manager" thing?
    # Q: Should be called "UserCollectionManager"?

    def set_library_controller(self, library_controller):
        # Q: Why set a library controller? Shouldn't I manage a UserCollection?
        raise NotImplementedError

    def create_user(self, user_id):
        # From the UML
        raise NotImplementedError
