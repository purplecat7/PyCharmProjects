from typing import Callable


class UserCollection(list):
    """
    A collection of library users
    """

    def add_user(self, user):
        """
        Add user to this UserCollection
        """
        self.append(user)

    def _get_user(self, user_id):
        (user, ) = filter(lambda user: user.id == user_id, self)
        return user

    def able_to_borrow(self, user_id, *rules: Callable) -> bool:
        """
        Is user eligible to borrow from library?
        """
        return self._get_user(user_id).able_to_borrow(*rules)

    def checkout_item(self, user_id, item):
        """
        checkout a library item
        """
        return self._get_user(user_id).checkout_item(item)

    def return_item(self, user_id, item_id):
        """
        return a library item
        """
        return self._get_user(user_id).return_item(item_id)

    def get_fine(self, user_id):
        """
        get the current fine owed by a user
        """
        return self._get_user(user_id).fine

    def pay_fine(self, user_id, amount):
        """
        pay some amount of fine owed by a user
        """
        return self._get_user(user_id).pay_fine(amount)
