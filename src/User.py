class User(object):
    """ A user/borrower in the library system"""

    def __init__(self):
        self._identification = self.set_id()
        self._ItemList = ItemCollection()
        self._fines = 0

    def set_id(self):
        """Set unique id for user"""
        raise NotImplementedError

    def get_id(self):
        """Return the ID for the user"""
        return self._identification

    def able_to_borrow(self, max_number_loans, max_total_fine):
        """Check if user is eligible to borrow
        :param max_number_loans: maximum number of items allowed out
        :param max_total_fine: maximum accrued fine allowed in order to borrow
        :return: Bool
        """
        raise NotImplementedError

    def checkout_item(self, item_requested, date):
        """Add item to checked out items list
        :param item_requested: item to be checked out
        :param date: the date of checkout
        :return: N/A
        """
        self._ItemList.add_item(item_requested, date)

    def return_item(self, item_id):
        """Remove item from user's item list
        :param item_id: ID of item to be returned
        :return: N/A
        """
        self._ItemList.return_item(item_id)

    def get_fines(self):
        """Check total fines for user
        :param: none
        :return: total fine owed by user
        """
        return self._ItemList.get_fines() + self._fines

    def pay_fine(self, amount):
        """Subtract paid amount from total
        :param amount: value of fine paid
        :return: N/A
        """
        self._fines = self._fines - amount
