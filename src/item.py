from __future__ import division
import datetime


class Item:
    """
    Abstract class for items in the library.

    --Public attributes--
        id_num (int)     : unique identifier for the item.
        title (str)      : title of item.
        checkout_date    : date at which item was checked-out
                           (datetime.datetime date object).
        available (bool) : True if available for checking out.

    --Public methods--
        get_identifier()    : return the ID number (int).
        get_title()         : return the title (str).
        get_checkout_date() : return the checkout date
                             (datetime.datetime date object).
        is_available()      : return whether available for checkout or
                              not (bool).
        get_fine_due()      : calculate the fine owed on this item.
        set_checkout()      : set the date of checkout and mark as
                              unavailable (no return).
        clear_checkout()    : check item in and clear checkout date
                              (no return).
    """

    def __init__(self, id_num, title):
        """Class initializer: declare instance variables. No return.

        --Arguments--
        id_num (int) : ID number.
        title (str)  : title of item.
        """
        self.id_num = id_num
        self.title = title
        self.checkout_date = None
        self.available = True
        pass

    def get_identifier(self):
        """Return the item ID number (int)."""
        return self.id_num

    def get_title(self):
        """Return the item title (str)."""
        return self.title

    def get_checkout_date(self):
        """Return the item checkout date (datetime.datetime date object)."""
        return self.checkout_date

    def is_available(self):
        """Return True if the item is available for checking out, else False."""
        return self.available

    def get_overdue_days(self):
        """Return the number of days item is overdue (int)."""
        if self.checkout_date is None:
            days_over = 0
        else:
            days_over = ((datetime.date.today() - self.checkout_date).days -
                        self.max_loan_time)
            days_over *= days_over > 0
        return days_over

    def get_fine_due(self):
        """Return the fine owed (float) in GBP on item."""
        return self.fee_rate*self.get_overdue_days()

    def set_checkout(self, the_date=datetime.date.today()):
        """Set the checkout date. No return.

        --Arguments--
        the_date: datetime module date object; by default this is
                  today's date but may be set by using

                      datetime.date(YEAR, MONTH, DAY)

                  where the YEAR, MONTH and DAY arguments are
                  integers (see datetime docs for further details).
        """
        if type(the_date) != datetime.date:
            raise TypeError('Checkout date must be a datetime.date object.')

        self.checkout_date = the_date
        self.available = False
        pass

    def clear_checkout(self):
        """Clear the checkout date and mark as available. No return."""
        self.checkout_date = None
        self.available = True
        pass


class Book(Item):
    """Book class (concrete, inherits from Item).

    --Additional public attributes--
        fee_rate (float)    : fee accrued in GBP per day over due-date.
        max_loan_time (int) : maximum number of days item can be on loan.
    """

    # Class attributes:
    fee_rate = 0.5  # GBP/day
    max_loan_time = 28  # days


class Dvd(Item):
    """DVD class (concrete, inherits from Item).

    --Additional public attributes--
        fee_rate (float)    : fee accrued in GBP per day over due-date.
        max_loan_time (int) : maximum number of days item can be on loan.
    """

    # Class attributes:
    fee_rate = 2.0  # GBP/day
    max_loan_time = 7  # days


class Journal(Item):
    """Journal article class (concrete, inherits from Item).

    --Additional public attributes--
        fee_rate (float)    : fee accrued in GBP per day over due-date.
        max_loan_time (int) : maximum number of days item can be on loan.
    """

    # Class attributes:
    fee_rate = 1.0  # GBP/day
    max_loan_time = 14  # days
