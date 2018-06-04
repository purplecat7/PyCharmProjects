from __future__ import division
from datetime import datetime

class Item():
    """
    Class for items in the library.

    Attributes:
        id            : int, unique identifier for the item.
        title         : str, title of item.
        checkout_date : date at which item was checked-out.
        checked_out   : bool, whether checked out or not.

    Methods:
        get_identifier()     : return the ID number attribute.
        get_title()          : return the title attribute.
        get_checkout_date () : return the checkout date attribute.
        get_fine_due()       : calculate the fine owed on this item.
        is_available()       : return True if available, False otherwise.
        set_checkout()       : set the date of checkout to today's date.
        clear_checkout()     : set the item to be not checked-out (i.e. check-
                               in) and clear checkout_date attribute.

    """

    def __init__(self, id, title, checkout_date):
        """Initialise instance variables.

        id : ID number.
        title: title of item.
        checkout_date: datetime-module date when checked out.
        """
        self.id = id
        self.title = title
        self.checkout_date = None
        self.checked_out = True
        pass

    def get_identifier(self):
        """Return the ID number."""
        return self.id

    def get_title(self):
        """Return the title."""
        return self.title

    def get_checkout_date(self):
        """Return the checkout date."""
        return self.checkout_date

    def get_fine_due(self):
        """Calculate the fine owed on this item."""
        days_overdue = datetime.today() - (self.checkout_date + self.max_loan_time)
        the_fine = self.fee_rate*days_overdue*(days_overdue>0)
        return the_fine

    def is_available(self):
        return not(self.checked_out == True)

    def set_checkout(self):
        """Set the checkout date somehow."""
        self.checkout_date = datetime.today()
        self.checked_out = True
        pass

    def clear_checkout(self):
        """Clear the checkout date somehow."""
        self.checkout_date = None
        self.checked_out = False
        pass


class Book(Item):
    """
    Book class, inherits from Item.

    Attributes:
        fee_rate      : float, over-due fee per day over due-date.
        max_loan_time : float, maximum number of days item can be on loan.
    """

    # Class attributes:
    fee_rate = 0.5 # GBP/day
    max_loan_time = 28 # days


class Dvd(Item):
    """
    DVD class, inherits from Item.

    Attributes:
        fee_rate      : float, over-due fee per day over due-date.
        max_loan_time : float, maximum number of days item can be on loan.
    """

    # Class attributes:
    fee_rate = 2.0 # GBP/day
    max_loan_time = 7  # days


class Journal(Item):
    """
    Journal article class, inherits from Item.

        Attributes:
        fee_rate      : float, over-due fee per day over due-date.
        max_loan_time : float, maximum number of days item can be on loan.
    """

    # Class attributes:
    fee_rate = 1.0 # GBP/day
    max_loan_time = 14 # days
