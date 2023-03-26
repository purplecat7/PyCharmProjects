from itemlist import ItemList
from library_exceptions import FineHighError, TooManyItems


class User:
    def __init__(self, user_id):
        self._fines = float()
        self._identification = int()
        self._item_list = ItemList()
        self.user_id = user_id

    def __del__(self):
        pass

    def able_to_borrow(self, max_number_loans, max_total_fine):
        # checks if user is able to borrow
        fine_total = self.get_fine_total()
        num_items = self._item_list.number_of_items()
        if num_items <= max_number_loans and fine_total <= max_total_fine:
            return True
        elif fine_total > max_total_fine:
            raise FineHighError(fine_total, max_total_fine - fine_total)
        elif num_items > max_number_loans:
            raise TooManyItems(num_items, max_number_loans)

    def checkout_item(self, item_requested, date):
        # checks out item
        self._item_list.append(item_requested)

    def get_fine_total(self):
        # returns the total amount of fines for the user
        return self._item_list.get_fines()

    def get_identification(self):
        return self._identification

    def pay_fine(self, amount):
        # subtracts amount from user's total fines
        self._fines = ItemList.get_fines(self._item_list) - amount
        pass

    def return_item(self):
        # updates user's returned item list
        return
