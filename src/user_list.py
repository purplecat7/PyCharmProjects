class UserList(list):
    """A list of library users"""

    def __init__(self):
        """Initialises a list of library users"""
        super().__init__()
        pass

    def add_user(self, new_user):
        """
        Adds a new user to the user list
        :param new_user: User object to be added to the user list
        :type new_user: Object of the user to be added to the user list
        :return: Nothing
        :rtype: Nothing
        """
        self.append(new_user)

    def able_to_borrow(self, user_id, max_loans, max_fine):
        """
        Checks if the user is able to borrow an item
        :param user_id: User ID
        :type user_id: int
        :param max_loans: Maximum loans set by library. User can only borrow if their loans is below max_loans
        :type max_loans: int
        :param max_fine: Maximum fine set by library. User can only borrow if their total fine is below max_fine
        :type max_fine: float
        :return: True if user is able to borrow, else False
        :rtype: bool
        """
        this_user = self._find_user(user_id=user_id)
        return this_user.able_to_borrow(max_number_loans=max_loans, max_total_fines=max_fine)

    def checkout_item(self, user_id, item_requested, date):
        """
        Checks out the requested item for the user
        :param user_id: User ID number
        :type user_id: int
        :param item_requested: Requested item for checking out
        :type item_requested: Item
        :param date: Checkout date
        :type date: datetime or str? #TODO: Decide on date format
        :return: Nothing
        :rtype: Nothing
        """
        this_user = self._find_user(user_id=user_id)
        this_user.checkout_item(item_requested=item_requested, date=date)

    def return_item(self, user_id, item_id):
        """
        Returns the item for the user
        :param user_id: User ID number that is returning the item
        :type user_id: int
        :param item_id: Item ID number for returning
        :type item_id: int
        :return: Nothing
        :rtype: Nothing
        """
        this_user = self._find_user(user_id=user_id)
        this_user.checkout_item(item_id=item_id)

    def get_fine_total(self, user_id):
        """
        Returns the total fine of the user
        :param user_id: User ID number that we would like to check the fine for
        :type user_id: int
        :return: Total fine associated with the User ID
        :rtype: float
        """
        this_user = self._find_user(user_id=user_id)
        return this_user.get_fine_total()

    def pay_fine(self, user_id, amount):
        """
        Settles fine with an amount for a user
        :param user_id: User ID number that we would like to settle fines for
        :type user_id: int
        :param amount: Amount the user is paying
        :type amount: float
        :return: Nothing
        :rtype: Nothing
        """
        this_user = self._find_user(user_id=user_id)
        return this_user.pay_fine(amount=amount)

    def _find_user(self, user_id):
        """
        Finds a user from the user list
        :param user_id: Identity number of the user to be found
        :type user_id: int
        :return: Object of the found user
        :rtype: User
        """
        for user in self:
            if user.user_ID == user_id:
                return user
