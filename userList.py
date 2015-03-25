class UserList(list):
    """ Will return a user object from a list of names
    """
    def __init__(self):
        self.user_list = list()

    def find_user(self, my_id):
        for x in self.user_list:
            if x == my_id:
                return x
            else:
                return None