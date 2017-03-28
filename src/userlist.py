
class UserList:
    def __init__(self):
        # self is an instance of UserList
        self.users_list = []

    def __del__(self):
        pass

    def _find_user(self, user_id):
        # searches user list
        for user in self.users_list:
            if user.user_id == user_id:
                return user

    def able_to_borrow(self):
        # checks if user is able to borrow
        return

    def add_user(self, user):
        # adds a user to the users_list
        return

    def checkout_item(self):
        # checks out item
        return

    def get_fine_total(self):
        # returns the total amount of fines for the user
        return

    def pay_fine(self):
        # updates whether or not a user has paid a fine
        return

    def return_item(self):
        # updates user's returned item list
        return
