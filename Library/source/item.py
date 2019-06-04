
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

        # possibly raise exception if date is not None

        self.checkout_date = date
        # set date that item is checked out


    def checkin_item(self, date):

        days_overdue = (today_date - self.checkout_date) - self.lend_time
        # calculate number of days item is overdue (may be negative)

        if days_overdue > 0:
            # if item is overdue

            fine = self.fine_rate * days_overdue
            # calculate fine due on item

        self.checkout_date = None
        # now item is returned reset checkout date to None

        return fine
        #