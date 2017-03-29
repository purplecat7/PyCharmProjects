"""
Class exceptions for the library system

"""

# item does not exist
# item on loan already
# pay too much money for fine
# already have books overdue
# user does not exist
# just dont like the person
# silly name/id

# Fine is too high!

class LibraryException(Exception):

    def __init__(self):
        pass


class FineHigh(LibraryException):

    """
    Exception when fine is too high!
    """

    def __init__(self, fine, fine_remaining):
        self.fine = fine
        self.fine_remaining = fine_remaining

    def __str__(self):
        return 'Your fine is ' + repr(self.fine) + ': Pay ' + str(self.fine_remaining) + ' fine to check out item.'


class TooManyItems(LibraryException):


    def __init__(self, user_items, max_items):
        self.user_items = user_items
        self.max_items = max_items

    def __str__(self):
        return 'You have borrowed ' + str(self.user_items)+ ', you are allowed' + str(self.max_items) + \
                                    ': Please bring back some items.'


