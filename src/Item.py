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
        It's the number of days an item can be loaned before being overdue.
        """
        pass

    @property
    @abstractmethod
    def finerate(self):
        """
        This gets overridden by child classes (e.g. Book)
        It's the charge per-overdue-day.
        """
        pass

    def __del__(self):
        pass

    def set_checkout(self, date: datetime):
        """
        Set the checkout_date to whatever's passed in.
        If it's not a datetime then get_fine_due will break.
        """
        self._checkout_date = date

    def reset_checkout(self):
        self._checkout_date = None

    def get_identifier(self, identifier_type):
        return self._identity

    def get_fine_due(self):
        time_checked_out = datetime.now() - self._checkout_date
        time_overdue = time_checked_out - self.loantime
        fine = self.finerate * time_overdue
        return fine

    def is_checked_out(self):
        return self._checkout_date is not None
