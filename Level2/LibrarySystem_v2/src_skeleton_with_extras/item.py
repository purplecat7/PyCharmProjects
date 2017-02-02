# coding=utf-8
"""
NAME
    item - implementation of Item class
FILE
    item.py
CLASSES
    Item
    Book
    Dvd
    Journal
"""

import datetime


class Item:
    """
    Base class to implement library items: Book, Dvd & Journa

    Methods defined here:

        set_checkout(...)
            Set the checkout date of item

        reset_checkout(...)
            Reset checkout date to NaN

        get_identifier(...)
            Given a identifier_type string of 'ID' or 'Title' returns title or id of item

        get_fine_due(...)
            Returns the amount of money due in fines on item

        is_checked_out(...)
            Query checkout status of item

    ----------------------------------------------------------------------
    No data or other attributes defined here.

    """
    def __init__(self, title, ident):
        self._title = title
        self._identity = ident
        self._checkout_date = None

    def __del__(self):
        pass

    def set_checkout(self, date=False):
        """
        Set the checkout date of item.

        :param date: optional, if provided then used, otherwise set to now
        :return: no return
        """

            
    def reset_checkout(self):
        # TODO Rename to cancel_checkout()
        """
        Reset checkout date to NaN

        :return: no return
        """

        
    def get_identifier(self, identifier_type):
        """
        Given a identifier_type string of 'ID' or 'Title' returns title or id of item.

        :param identifier_type: either of 'ID' or 'Title'
        :return: unique id or title of item
        :rtype: int or string
        """
        if identifier_type == 'ID':
            return self._identity
        elif identifier_type == 'Title':
            return self._title
                        
    def get_fine_due(self):
        """
        Returns the amount of money due in fines on item.

        :return: calculated fine
        :rtype: float
        """
        # get timestamp for 'now' and for checkout, and calculate difference (in days)
        # do the maths on the days overdue and return the amount


    def is_checked_out(self):
        """
        Query checkout status of item.

        :return: True if item is on loan, False otherwise
        """

            
class Book(Item):
    """
    Book class: derived from Item.
    No methods defined here.
    ----------------------------------------------------------------------
    Attributes defined here:
        finerate:
            Rate at which a book accrues fine when overdue

        loantime:
            Limit of loan before fines apply
    """
    finerate = 0.50  # 50p/day
    loantime = 4*7  # 4 weeks
        

class Journal(Item):
    """
    Journal class: derived from Item.
    No methods defined here.
    ----------------------------------------------------------------------
    Attributes defined here:
        finerate
            Rate at which a book accrues fine when overdue

        loantime
            Limit of loan before fines apply
    """
    finerate = 1.0  # £1/day
    loantime = 2*7  # 4 weeks
        
        
class Dvd(Item):
    """
    Dvd class: derived from Item.
    No methods defined here.
    ----------------------------------------------------------------------
    Attributes defined here:
        finerate
            Rate at which a book accrues fine when overdue

        loantime
            Limit of loan before fines apply
    """
    finerate = 2.0  # £2/day
    loantime = 1*7  # 4 weeks
