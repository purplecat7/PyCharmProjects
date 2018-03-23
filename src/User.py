from src import ItemCollection as im


class User:
    """ A user/borrower in the library system"""

    def __init__(self, user_id):
        self._identification = user_id
        self._ItemList = im.ItemCollection()
        self._fines = 0

    def get_id(self):
        """Return the ID for the user"""
        return self._identification

    def able_to_borrow(self, *rules):
        """Check if user is eligible to borrow
        :param rules: business rules
        :return: Bool
        """
        eligible = True
        for rule in rules:
            if rule(self) is False:
                eligible = False
        return eligible

    def checkout_item(self, item_requested, date):
        """Add item to checked out items list
        :param item_requested: item to be checked out
        :param date: the date of checkout
        :return: N/A
        """
        item_requested.set_checkout(date)
        self._ItemList.add_item(item_requested)

    def return_item(self, item_id, date):
        """Remove item from user's item list
        :param item_id: ID of item to be returned
        :param date: date of return
        :return: N/A
        """
        item = self._ItemList.get_item(item_id)
        self._ItemList.return_item(item, date)

    def get_fines(self):
        """Check total fines for user
        :param: none
        :return: total fine owed by user
        """
        return self._ItemList.get_fines()

    def pay_fine(self, amount):
        """Subtract paid amount from total
        :param amount: value of fine paid
        :return: N/A
        """
        self._fines = self._fines - amount

    def get_number_loans(self):
        """Get number of items currently borrowed
        :param:
        :return n_loans: number of items currently borrowed
        """
        return self._ItemList.number_of_items
