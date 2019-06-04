
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


    def setdate(self, date=datetime.date.today()):
        """
        Set the date attribute of item to given date (on which item is checked out)
        :param date: datetime object of today's date
        """

        # possibly raise exception if date is not None

        self.checkout_date = date
        # set date that item is checked out


    def checkin_item(self, date=datetime.date.today()):
        """
        Calculate fine resultant from item being overdue (if any)
        Set checkout_date to None, as item is no longer checked out
        :param date: datetime object of today's date
        :return: float, fine in pounds to be added to user's accrued fine due to the overdue return of this item
        """

        days_overdue = self.find_days_overdue(self, date)

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


    def find_days_overdue(self, date=datetime.date.today()):
        """
        Calculate number of days by which item is overdue
        If item is not overdue returns zero
        :param date: datetime object of today's date
        :return: float, number of days overdue
        """

        days_overdue = (date - self.checkout_date) - self.lend_time
        # calculate number of days item is overdue (may be negative)
        # will be timedelta object

        return days_overdue.days
        # return float number of days


    def is_overdue(self, date=datetime.date.today()):
        """
        Determine whether item is overdue
        :param date: datetime object of today's date
        :return: bool, if item is overdue
        """

        days_overdue = self.find_days_overdue(self, date)

        if days_overdue > 0:

            overdue = True

        else:

            overdue = False

        return overdue
        # if it is positive number of days overdue, then overdue is True


    def is_onloan(self):
        """
        Determine whether item is on loan
        :return: bool, if item is on loan
        """

        if self.checkout_date == None:

            onloan = False

        elif isinstance(self.checkout_date, datetime.datetime):

            onloan = True

        return onloan
        # if it has a checkout date, it is on loan. If it doesn't, it is not



class Book(Item):

    lend_time = datetime.timedelta(weeks = 4)
    fine_rate = .5
    # fine rate 50p per day, loan period 4 weeks


class DVD(Item):

    lend_time = datetime.timedelta(weeks=1)
    fine_rate = 2
    # fine rate £2 per day, loan period 1 week


class Journal(Item):

    lend_time = datetime.timedelta(weeks=2)
    fine_rate = 2
    # fine rate £2 per day, loan period 2 weeks





