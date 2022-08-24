""" Creating classes for DVD's, books and Journals. """


# ---------------------------------------------------------------------------------------------------------------
class journal:
    # Defining class attribute: fine rate to be paid once overdue instance attribute: title, checkout date
    Attributes_dict = {}

    # Method to be called whenever new instance is created
    def __init__(self):
        # Initialise instance attributes
        self.__privateAttribute = 0
        self.__privateAttribute = list()

    # Method called when object destroyed
    def __del__(self):
        self.__privateList = None

    # Method to compute fine once overdue
    def compute_fine(self, fine_rate, checkout_date, current_date):
        """ Computes fine accrued for a given instance based upon how long after the checkout date the current date is
    """

# ------------------------------------------------------------------------------------------------------------
class DVD:

    # Defining class attribute: fine rate to be paid once overdue instance attribute: title, checkout date
    Attributes_dict = {}

    # Method to be called whenever new instance is created
    def __init__(self):
        # Initialise instance attributes
        self.__privateAttribute = 0
        self.__privateAttribute = list()

    # Method called when object destroyed
    def __del__(self):
        self.__privateList = None

    # Method to compute fine once overdue
    def compute_fine(self, fine_rate, checkout_date, current_date):
        """ Computes fine accrued for a given instance based upon how long after the checkout date the current date is
    """

# ------------------------------------------------------------------------------------------------------------------
class book:

    # Defining class attribute: fine rate to be paid once overdue instance attribute: title, checkout date
    Attributes_dict = {}

    # Method to be called whenever new instance is created
    def __init__(self):
        # Initialise instance attributes
        self.__privateAttribute = 0
        self.__privateAttribute = list()

    # Method called when object destroyed
    def __del__(self):
        self.__privateList = None

    # Method to compute fine once overdue
    def compute_fine(self, fine_rate, checkout_date, current_date):
        """ Computes fine accrued for a given instance based upon how long after the checkout date the current date is
    """




