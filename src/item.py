import arrow

class Item:

    # Initialise instance attributes
    def __init__(self, ID, Title):
        self.ID = ID
        self.Title = Title
        self.checkout_date = None
        self.finerate = None
        self.loantime = None


    # Class methods
    def set_checkoutdate(self, past_date=None):
        """
        Sets the checkout date when the item is checked out
        :param past_date
        """
        if past_date is not None:
            self.checkout_date = arrow.utcnow()
        else:
            self.checkout_date = past_date

    def get_ID(self):
        """
        :return: ID
        """
        return self.ID

    def get_Title(self):
        """
        :return: Title
        """
        return self.Title

    def reset_checkoutdate(self):
        """

        """
        self.checkout_date = None

    def is_checked_out(self):
        """

        :return:
        """
        if self.checkout_date is not None:
            return True
        else:
            return False

    def how_long_loaned(self,return_date):
        """

        :return:
        """
        if return_date is None:
            return_date = arrow.utcnow()
        loan_length = return_date - self.checkout_date
        return loan_length

    def calc_finedue(self, return_date=None):
        """

        :return:
        """
        loan_length = self.how_long_loaned(return_date)

        fine_due = self.finerate * (loan_length - self.loantime)
        if fine_due < 0:
            fine_due = 0

        return fine_due

    def check_item_fined(self):
        """

        :return:
        """
        if self.calc_finedue:
            return True
        else:
            return False























