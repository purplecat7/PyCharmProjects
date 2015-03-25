class UserList(dict):
    """ Will return a user object from a list of names
    """

    def find_user(self, user):
        for x in user.dict:
            if x == user.identification:
                return x
            else:
                return None