from user import User
from library_system import LibrarySystem

class UserInitialise:

    def __init__(self, library_system):
        from main import NumbID
        self.libsys = library_system
        self.IDgen = NumbID()

    def __del__(self):

        pass


    def add_new_user(self, username):
        """
        Creates single item of specified type and adds to list
        :param username: string, name of user
        """

        new_user = User(username, self.IDgen.new_id())
        # create object of class User, assigning a unique id number & name

        self.libsys.add_new_user(new_user)
        # tell libsys to add object to given UserList