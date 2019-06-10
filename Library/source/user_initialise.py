from user import User

class UserInitialise():

    def __init__(self):

        pass


    def __del__(self):

        pass


    def load_new_user(self, userlist, username):
        """
        Creates single item of specified type and adds to list
        :param userlist: UserList object to add users to
        :param username: string, name of user
        """

        # create object of class User, assigning a unique id number & name

        # add object to given UserList