from abc import abstractmethod
from datetime import datetime


class Item:
    def __init__(self, title, ident):
        self._title = title
        self._identity = ident
        self._checkout_date = None

    @property
    @abstractmethod
    def loantime(self):
        """
        This gets overridden by child classes (e.g. Book)
        :return: The number of days an item can be loaned before being overdue.
        """
        pass

    @property
    @abstractmethod
    def finerate(self):
        """
        This gets overridden by child classes (e.g. Book)
        :return: The charge per-overdue-day.
        """
        pass

    def __del__(self):
        pass

    def set_checkout(self, date: datetime):
        """
        Set the checkout_date to whatever's passed in.
        :param date: Date of checkout (probably today)
        :raises: ValueError if the date isn't a datetime.datetime object
        """
        if date is None:
            date = datetime.now()
        if type(date) is not datetime:
            raise ValueError
        self._checkout_date = date

    def reset_checkout(self):
        self._checkout_date = None

    def get_identifier(self, identifier_type):
        return self._identity

    def get_fine_due(self):
        if not self.is_checked_out():
            raise Exception(
                    "Can't get the fines of an item which isn't checked out")
        time_checked_out = datetime.now() - self._checkout_date
        days_overdue = time_checked_out.days - self.loantime
        fine = self.finerate * days_overdue
        return fine

    def is_checked_out(self):
        return self._checkout_date is not None

    def get_title(self):
        return self._title


class Book(Item):
    @property
    def finerate(self):
        """
        :return: The charge per-overdue-day.
        """
        return 0.5

    @property
    def loantime(self):
        """
        :return: The number of days an item can be loaned before being overdue.
        """
        return 4*7


class Journal(Item):
    @property
    def finerate(self):
        """
        :return: The charge per-overdue-day.
        """
        return 1.0

    @property
    def loantime(self):
        """
        :return: The number of days an item can be loaned before being overdue.
        """
        return 2*7


class Dvd(Item):
    @property
    def finerate(self):
        """
        :return: The charge per-overdue-day.
        """
        return 2.0

    @property
    def loantime(self):
        """
        :return: The number of days an item can be loaned before being overdue.
        """
        return 1*7
