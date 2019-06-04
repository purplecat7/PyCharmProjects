
import datetime
# I would like all dates and periods of time as datetime and timedelta objects

class Item():


    def __init__(self, name, id):

        self.name = name
        self.id = id
        self.checkout_date = None
        # initialise attributes common to all items


    def __del__(self):

        pass
        # delete an item


    def setdate(self, date):
        """
        Set the date attribute of item to given date (on which item is checked out)
        :param date: datetime object of today's date
        """

        # possibly raise exception if date is not None

        self.checkout_date = date
        # set date that item is checked out


    def checkin_item(self, date):
        """
        Calculate fine resultant from item being overdue (if any)
        Set checkout_date to None, as item is no longer checked out
        :param date: datetime object of today's date
        :return:
        """

        days_overdue = (today_date - self.checkout_date) - self.lend_time
        # calculate number of days item is overdue (may be negative)

        fine = 0

        if days_overdue > 0:
            # if item is overdue

            fine = self.fine_rate * days_overdue
            # calculate fine due on item

        self.checkout_date = None
        # now item is returned reset checkout date to None

        return fine
        # the method checkin_item will return to the caller the fine which needs to be added to the User's fine accrued
        # if the item was not everdue this will return zero (so may as well be added)


    def days_overdue(self, date):
        """
        Calculate number of days by which item is overdue
        If item is not overdue returns zero
        :param date: datetime object of today's date
        :return: int, number of days overdue
        """

        days_overdue = (today_date - self.checkout_date) - self.lend_time
        # calculate number of days item is overdue (may be negative)
        # will be timedelta object

        return days_overdue.days
        # return integer number of days


    def is_overdue(self, date):
        """

        :param date:
        :return:
        """



