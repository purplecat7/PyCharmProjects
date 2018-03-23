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
        :param max_number_loans: maximum number of items allowed out
        :param max_total_fine: maximum accrued fine allowed in order to borrow
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
        item = self._ItemList.get_item(item_requested)
        item.set_checkout(date)

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
        items = self._ItemList._items
        fine = 0
        for item in items:
            fine = fine + item.get_fine_due()
        return fine + self._fines

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
