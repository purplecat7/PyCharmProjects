"""
Used to add users to the library
"""
from src.library import Library
from src.user import User
from src.main import NumID


class UserBuilder:

    def __init__(self, file_path):
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
        :param title: A string
        """
        self.library.add_user(User(NumID.new_id()))
