"""
Used to add users to the library
"""
from LibSys_2022_alexandria.src.user import User
from LibSys_2022_alexandria.src.numbid import NumbID


class UserBuilder:

    def __init__(self):
        self.library = None

    def set_library(self, library):
        """
        Set the library that we want to pass users too!
        :param library: Target library object
        """
        self.library = library

    def create_user(self):
        """
        Creates a user and gives it to the target library
        """
        self.library.add_user(User(NumbID.new_id()))
