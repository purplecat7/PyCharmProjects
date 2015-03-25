import itemList


class User(object):
    """
    Class to create user for
    the library application
    """

    def __init__(self):
        self._identification = int()
        self._user_items = itemList.UserItemList()

    def __del__(self):
        pass

    # Set up the getter and the setter
    # for defining the user ID when the
    # user is created or searched for

    def get_identification(self):
        """
        Gets the user id
        """
        return self._identification

    def set_identification(self, value):
        """
        Sets the user id
        """
        self._identification = value

    # Method to decide whether or not the
    # user can borrow an item based on whether
    # the maximum number of loanable items is
    # exceeded or maximum total fine is exceeded

    def able_to_borrow(self, max_number_loans, max_total_fine):
        current_loans = self._user_items.GetFines()
        current_fines = self._user_items.NumberOfItems()

        # assess whether user can borrow
        too_many_loans = current_loans >= max_number_loans
        too_much_fine = current_fines >= max_total_fine
        if too_many_loans or too_much_fine:
            return False  # cannot borrow
        else:
            return True  # can borrow

    # Method to loan an item to the user.

    def loan_item(self, item_id):
        self._user_items.add_item(item_id)

if __name__ == "__main__":
    pass
