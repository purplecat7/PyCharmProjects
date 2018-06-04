class Item():
    """
    Class for items in the library.

    Attributes:
        id            : int, unique identifier for the item.
        title         : str, title of item.
        checkout_date : date at which item was checked-out.

    Methods:
        get_fine()       : calculate the fine owed on this item.
        set_checkout()   : set the date of checkout
        clear_checkout() : set the item to be not checked-out (i.e. check-in).

    """

    def __init__(self, id, title, checkout_date):
        self.id = id
        self.title = title
        self.checkout_date = checkout_date
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
        the_fine = 0.0
        return the_fine

    def set_checkout(self):
        """Set the checkout date somehow."""
        pass

    def clear_checkout(self):
        """Clear the checkout date somehow."""
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
