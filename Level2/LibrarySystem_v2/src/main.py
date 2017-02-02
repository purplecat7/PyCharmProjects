# coding=utf-8
"""
NAME
    main - library system program
FILE
    main.py
CLASSES
    NumID
"""
import item_manager as im
import user_manager as um
import library
import datetime as dt
import lib_exceptions

class NumbID:
    """
    Utility class to provide unique identifier.

    Methods defined here:
        new_id(...)
            Provide next unique identifier, starts at 1.

        reset_id(...)
            Reset unique identifier.
    """
    id_number = 0

    def __init__(self):
        pass

    def __del__(self):
        pass

    # note that these use the @staticmethod adornment since no instance
    # attributes are used.
    @staticmethod
    def new_id():
        NumbID.id_number += 1
        return NumbID.id_number

    @staticmethod
    def reset_id():
        NumbID.id_number = 0


def create_library_catalogue(lib_controller, infile):
    """
    Populate library's list of loanable items.

    :param lib_controller: LibraryController object
    :param infile: text file containing book titles
    :return: no return
    """
    item_manager = im.ItemManager()
    item_manager.set_library_controller(lib_controller)
    file_ = open(infile, 'r')
    for line in file_:
        item_manager.create_book(line.strip(), NumbID.new_id())
    print 'Number of books added: ', NumbID.id_number
    item_manager.create_journal("Amazing Clouds", NumbID.new_id())
    item_manager.create_journal("Sleuthing in C#", NumbID.new_id())
    item_manager.create_dvd("Dad's Army", NumbID.new_id())
    item_manager.create_dvd("Debugging to music", NumbID.new_id())
    print 'Total number of items: ', NumbID.id_number


def create_library_members(lib_controller):
    """
    Create some users for the library system's list.

    :param lib_controller: LibraryController object
    :return: no return
    """
    user_manager = um.UserManager()
    user_manager.set_library_controller(lib_controller)
    NumbID.reset_id()
    # create 4 users
    for count in range(0, 4):
        user_manager.create_user(NumbID.new_id())
        print 'User ID created: ', NumbID.id_number


def exercise1(user_id, title, lib_controller):
    """
    Checkout an item.

    :param user_id: user's unique identifier
    :param title: item to borrow
    :param lib_controller: LibraryController object
    :return: no return
    """
    lib_controller.user_checkout(user_id, title)


def exercise2(user_id, return_id, title, lib_controller):
    """
    Return an item and checkout another.

    :param user_id: user's unique identifier
    :param return_id: unique id of item returned
    :param title: item to borrow
    :param lib_controller: LibraryController object
    :return: no return
    """
    fine = lib_controller.user_fine(user_id)
    print "User: ", user_id
    print "Total Fine: ", fine
    
    lib_controller.user_return(user_id, return_id)
    lib_controller.user_checkout(user_id, title)


def johnny_codewarrior(lib_controller):
    """
    Use case 1: user with no accrued fines, one book out (not overdue)
    checks out "Document, Your job depends on it"
    :param lib_controller: LibraryController object
    :return:
    """
    try:
        # set up Johnny with a book already checked out, which obviously can't be overdue.
        # he'll not have any accrued fines either
        lib_controller.user_checkout(1, "The Curious Incident of the Dog in the Night-time")
        # now get the new book
        lib_controller.user_checkout(1, "Document, Your job depends on it")
        fine = lib_controller.user_fine(1)
        print "User: Johnny, ID ", str(1)
        print "Total Fine: ", fine
    except lib_exceptions.CannotBorrowException:
        print ("User 1 may not borrow book")


def judy_hacker(lib_controller):
    """
    Use case 2: user has fines of £2, has one book out (not overdue),
    bringing back a journal, and would like a DVD.
    :param lib_controller: LibraryController object
    :return:
    """
    try:
        # set up Judy with a book, an overdue journal, and with an accumulated fine
        lib_controller.user_checkout(2, "The Time Traveler's Wife")
        # we can make the journal overdue using the optional 'date' parameter in the library's checkout method
        lib_controller.user_checkout(2, "Sleuthing in C#", date=(dt.datetime.now() - dt.timedelta(days=16)))
        # we can be certain of a fine of £2 by having a book overdue by 4 days
        # but immediately return it to comply with the scenario
        lib_controller.user_checkout(2, "Atonement", date=(dt.datetime.now() - dt.timedelta(days=32)))
        lib_controller.user_return(2, 22)
        # now bring back the journal - which will have added to our fine total
        lib_controller.user_return(2, 102)
        # and finally, ask for the DVD - hopefully the accrued fines don't prevent it!
        lib_controller.user_checkout(2, "Debugging to music")

        fine = lib_controller.user_fine(2)
        print "User: Judy, ID ", str(2)
        print "Total Fine: ", fine

    except lib_exceptions.CannotBorrowException:
        print ("User 2 may not borrow DVD")


def miss_marple(lib_controller):
    """
    Use case 3: user cannot find journal so needs to find out if it's already out.
    :param lib_controller: LibraryController object
    :return:
    """
    # let's set up this item as loaned out to someone else
    lib_controller.user_checkout(2, "Sleuthing in C#")
    # now we'll do the query
    status = lib_controller.is_on_loan("Sleuthing in C#")
    if status:
        print("Sleuthing in C# already on loan.")
    else:
        print("Sleuthing in C# available.")
    # now let's return it and try again
    lib_controller.user_return(2, 102)
    status = lib_controller.is_on_loan("Sleuthing in C#")
    if status:
        print("Sleuthing in C# already on loan.")
    else:
        print("Sleuthing in C# available.")

def eric_halfbee(lib_controller):
    """
    Use case 4: user returns overdue items but needs to be able to pay off before borrowing DVD.
    :param lib_controller: LibraryController object
    :return:
    """
    try:
        # Let's borrow a few books, make their checkout date ages ago...
        lib_controller.user_checkout(4, "The Da Vinci Code", date=(dt.datetime.now() - dt.timedelta(days=75)))
        lib_controller.user_checkout(4, "Harry Potter and the Philosopher's Stone", date=(dt.datetime.now() - dt.timedelta(days=55)))
        lib_controller.user_checkout(4, "Harry Potter and the Chamber of Secrets", date=(dt.datetime.now() - dt.timedelta(days=65)))
        fine = lib_controller.user_fine(4)
        print "User: Eric, ID ", str(4)
        print "Total Fine: ", fine
        # try to borrow something - this should throw an exception since Eric owes a pile of dosh...
        lib_controller.user_checkout(4, "Angels and Demons")

    except lib_exceptions.CannotBorrowException as e:
        print(e.message)

    try:
        # so now pay off some of the money
        lib_controller.pay_fine(4, 35.50)
        fine = lib_controller.user_fine(4)
        print "User: Eric, ID ", str(4)
        print "Total Fine: ", fine
        # and try again
        lib_controller.user_checkout(4, "Angels and Demons")
        lib_controller.user_checkout(4, "Dad's Army")
        print "Borrowed trashy novel & DVD successfully"

    except lib_exceptions.CannotBorrowException as e:
        print(e.message)

def main():
    """
    Program initialisation and execution.
    :return: no return
    """
    print "Initialising library controller..."
    lib_controller = library.LibraryController()

    print "Populating library catalogue..."
    infile = 'top100t.txt'
    try:
        create_library_catalogue(lib_controller, infile)
    except:
        print "Catalogue populating failed"
        raise

    print "Populating library members..."
    try:
        create_library_members(lib_controller)
    except:
        print "User populating failed"
        raise

    print "Exercise 1..."
    try:
        exercise1(1, 'The Kite Runner', lib_controller)
    except:
        print "Exercise 1 failed"
        raise

    print "Exercise 2..."
    try:
        exercise2(1, 19, 'Sleuthing in C#', lib_controller)
    except:
        print "Exercise 2 failed"
        raise

    try:
        johnny_codewarrior(lib_controller)
    except:
        print "Johnny Codewarrior failed"
        raise

    try:
        judy_hacker(lib_controller)
    except:
        print "Judy Hacker failed"
        raise


    try:
        miss_marple(lib_controller)
    except:
        print "Miss Marple failed"
        raise

    try:
        eric_halfbee(lib_controller)
    except:
        print "Eric Halfbee failed"
        raise


if __name__ == '__main__':
    main()
