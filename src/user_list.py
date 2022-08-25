class UserList(list):
    """A list of library users"""
    pass

    def __init__(self):
        """Initialises a list of library users"""
        super().__init__()
        pass

    def add_user(self, user_object):
        """
        Adds a new user to the user list
        :param user_object: Identity number of the user to be found
        :type user_object: Object of the user to be added to the user list
        :return: Nothing
        :rtype: Nothing
        """
        pass

    def find_user(self, user_id):
        """
        Finds a user from the user list
        :param user_id: Identity number of the user to be found
        :type user_id: int
        :return: Object of the found user
        :rtype: User
        """
        pass

if __name__ == '__main__':
    ul = UserList()
