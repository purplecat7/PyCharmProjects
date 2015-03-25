class UserList(object):
    """ Will return a user object from a list of names
    """

    def __init__(self):
        self.users = dict()

    def find_user(self, user_id):
        if user_id in self.users.keys():
            return self.users[user_id]
        else:
            raise ValueError('User Not Found')

    def add_user(self, new_user):
        assert isinstance(new_user.identification, object)
        assert isinstance(new_user, object)
        self.users[new_user.identification] = new_user