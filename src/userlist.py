import datetime as dt
from library_exceptions import UserNotExist

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
        raise UserNotExist(user_id)

    def able_to_borrow(self, user_id, max_number_loans, max_total_fine):
        # checks if user is able to borrow
        user = self._find_user(user_id)
        return user.able_to_borrow(max_number_loans, max_total_fine)

    def add_user(self, new_user):
        # adds a user to the users_list
        # open txt file containing users
        self.users_list.append(new_user)
        return

    def checkout_item(self,user_id, item):
        # checks out item
        user = self._find_user(user_id)
        user.checkout_item(item, dt.datetime.now())

    def get_fine_total(self, user_id):
        # returns the total amount of fines for the user
        user = self._find_user(self, user_id)
        user.get_fine_total(self)
        pass

    def pay_fine(self, user_id, amount):
        user = self._find_user(self, user_id)
        user.pay_fine(self, amount)
        # updates whether or not a user has paid a fine
        return

    def return_item(self, item_id, user_id):
        # updates user's returned item
        user = self._find_user(self, user_id)
        user.return_item(self, item_id)
        return
