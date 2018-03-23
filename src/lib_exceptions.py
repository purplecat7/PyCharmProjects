
class CannotBorrowException(Exception):
    def __init__(self):
        # print ('init CannotBorrowException')
        self.message = "Not allowed to borrow: too many items or too much fine due."

    def __str__(self):
        return repr(self.message)