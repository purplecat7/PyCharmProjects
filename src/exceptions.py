""" Class exceptions for the library system """


class LibraryException(Exception):
    def __init__(self):
        self.err = 'LibraryException'

    def __str__(self):
        print self.err


class FineHighError(LibraryException):
    """ You have surpassed the maximum fine limit. """
    def __init__(self, fine, fine_remaining):
        self.fine = fine
        self.fine_remaining = fine_remaining

    def __str__(self):
        return 'Your fine is ' + repr(self.fine) + ': Pay ' + str(self.fine_remaining) + ' fine to check out item.'


class TooManyItems(LibraryException):
    """ Exception for having borrowed too many items """
    def __init__(self, user_items, max_items):
        self.user_items = user_items
        self.max_items = max_items

    def __str__(self):
        return 'You have borrowed ' + str(self.user_items)+ ', you are allowed' + str(self.max_items) + \
                                    ': Please bring back some items.'


class ItemDoesNotExist(LibraryException):
    """ Item id does not exist """
    def __init__(self, item_id):
        self.item_id = item_id

    def __str__(self):
        return 'The item: ' + str(self.item_id) + ' does not exist! Please choose another item'


class ItemAlreadyOnLoan(LibraryException):
    """ Item is already on load """
    def __init__(self, item_id):
        self.item_id = item_id

    def __str__(self):
        return 'The item: ' + str(self.item_id) + ' is already on loan! Please choose another item'


class PayTooMuchForFine(LibraryException):
    """ Paying too much for their fine. """
    def __init__(self, fine):
        self.fine = fine

    def __str__(self):
        return 'Keep your money to yourself! Silly fool!'



class AlreadyOverdueItems(LibraryException):
    """ You already have overdue items and cannot take out more """
    def __init__(self, user_items):
        self.user_items = user_items

    def __str__(self):
        return 'You have ' + str(self.user_items) + ' overdue items and cannot take out more!'


class UserNotExist(LibraryException):
    """ User does not exist """
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return 'I see dead people... user does not exist! Please try again.'


class UserIdNotUnique(LibraryException):
    """ User id not unique """
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return 'I see dead people... user does not exist! Please try again.'


class DontLikePerson(LibraryException):
    """ Just don't like the person """
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return 'We just don''t like you ' + str(self.user_id) + '...'
        print super(DontLikePerson, self).__str__()
