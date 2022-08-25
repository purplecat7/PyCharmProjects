# import arrow
from datetime import datetime, timedelta

class Item:

    # Initialise instance attributes
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.checkout_date = None

    # Class methods
    def set_checkoutdate(self, past_date=None):
        """
        Sets the checkout date
        :param past_date
        """
        if past_date is not None:
            self.checkout_date = datetime.now()
        else:
            self.checkout_date = past_date

    def get_id(self):
        """
        Return the item id
        :return: id
        """
        return self.id

    def get_title(self):
        """
        Returns the item title
        :return: title
        """
        return self.title

    def reset_checkoutdate(self):
        """
        Resets the checkout date
        """
        self.checkout_date = None

    def is_checked_out(self):
        """
        Checks if an item is checked or not
        :return: True if item is checked out, False if it isn't checked out
        """
        if self.checkout_date is not None:
            return True
        else:
            return False

    def how_long_loaned(self):
        """
        Calculates the number of days the item has been loaned for
        :return: loan length as datetime
        """
        loan_length = datetime.now() - self.checkout_date

        return loan_length

    def calc_finedue(self):
        """
        Calculates the fine on an overdue item
        :param: return date
        :return: fine due
        """
        loan_length = self.how_long_loaned()

        fine_due = self.fine_rate * (loan_length - timedelta(days=self.max_loan_time)).days
        if fine_due < 0:
            fine_due = 0

        return fine_due

    def check_item_fined(self):
        """
        Checks if overdue time is fined
        :return: True if item overdue is fined, False if it isn't fined
        """
        if self.calc_finedue:
            return True
        else:
            return False