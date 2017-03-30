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

        cancel_checkout(...)
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

    def __del__(self):
        pass

    def set_checkout(self, date=False):
        """
        Set the checkout date of item.

        :param date: optional, if provided then used, otherwise set to now
        :return: no return
        """
            
    def cancel_checkout(self):
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

    def get_fine_due(self):
        """
        Returns the amount of money due in fines on item.

        :return: calculated fine
        :rtype: float
        """


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

