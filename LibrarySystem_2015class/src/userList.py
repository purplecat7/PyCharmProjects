import UserIdError

class UserList(object):
    """ Will return a user object from a list of names
    """

    def __init__(self):
        self.users = dict()

    def find_user(self, user_id):
        if user_id in self.users.keys():
            return self.users[user_id]
        else:
            raise UserIdError.UserIdError('User Not Found')

    def add_user(self, new_user):
        self.users[new_user.get_identification()] = new_user