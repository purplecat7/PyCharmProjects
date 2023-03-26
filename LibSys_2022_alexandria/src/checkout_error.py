
class MaxLoansExceededError(Exception):

    def __init__(self):
        self.message = "Cannot checkout. User has exceeded the maximum number of loans"

    def __str__(self):
        return repr(self.message)

class MaxFinesExceededError(Exception):

    def __init__(self):
        self.message = "Cannot checkout. User has exceeded the maximum fines"

    def __str__(self):
        return repr(self.message)

class CannotBorrowError(Exception):

    def __init__(self):
        self.message = "Cannot checkout."

    def __str__(self):
        return repr(self.message)

class NotFoundError(Exception):

    def __init__(self):
        self.message = "The thing you seek is not here."

    def __str__(self):
        return repr(self.message)