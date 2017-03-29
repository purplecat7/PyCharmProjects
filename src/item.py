import datetime as dt

class Item:
    """An object representing an item available for lending/borrowing within the library."""
    def __init__(self, title, ident):
        """Inputs:
            - title; a string representing the title of the item
            - ident; an integer representing the ID number of the item
        Sets the _checkout_date, _title and _identity attributes of Item.
        _checkout_date is set as None (until set_checkout method is used),
        _title is set as the title argument passed in the constructor,
        _identity is set as the indent argument passed in the constructor."""
        self._checkout_date = None
        self.loantime = None
        self.finerate = None
        if type(title) == str:
            self._title = title
        else:
            raise TypeError('title (arg1) should be of type string')
        if type(ident) == int:
            self._identity = ident
        else:
            raise TypeError('ident (arg2) should be of type int')


    def __del__(self):
        """Deletes the Item and its associations."""
        pass
    def get_fine_due(self):
        """Calculates the fine due for this item. Fine is calculated based on the number of
        days since the due date, multiplied by the fine rate (per day)."""
        fine = 0
        ndays = (dt.datetime.now() - self._checkout_date).days
        ndays_over = ndays - self.loantime
        if ndays_over > 0:
            fine += (ndays_over * self.finerate)
        return fine


    def get_identifier(self, identifier_type):
        """Finds the type of Item which is being dealt with."""
        if identifier_type == 'ID':
            retval = self._identity
        elif identifier_type == 'Title':
            retval = self._title
        else:
            raise ValueError('identifier_type is neither \'ID\' nor \'Title\'')
        return retval
    def is_checked_out(self):
        """Returns True if checked out, returns False otherwise."""
        return self._checkout_date is not None
    def reset_checkout(self):
        """Checks book back in; _checkout_date is restored to None."""
        self._checkout_date = None
    def set_checkout(self, date):
        """Sets the current date as the checkout date"""
        if type(date) != dt.datetime:
            raise TypeError('date must be a datetime.datetime object')
        else:
            pass
        self._checkout_date = date