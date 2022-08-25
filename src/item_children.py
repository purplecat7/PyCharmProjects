""" Defining classes for DVD, books and Journals. """


class Journal:
    # Defining class attributes: fine rate (£ per day) and max_loan_time (days)
    fine_rate = 1.0
    max_loan_time = 14

    # Method to be called whenever new instance is created
    def __init__(self):

        pass

    # Method called when object destroyed
    def __del__(self):

        pass


# ------------------------------------------------------------------------------------------------------------
class DVD:

    # Defining class attributes: fine rate (£ per day) and max_loan_time (days)
    fine_rate = 2.0
    max_loan_time = 7

    # Method to be called whenever new instance is created
    def __init__(self):

        pass

    # Method called when object destroyed
    def __del__(self):

        pass


# -----------------------------------------------------------------------------------------------------------------
class Book:

    # Defining class attributes: fine rate (£ per day) and max_loan_time (days)
    fine_rate = 0.5
    max_loan_time = 28

    # Method to be called whenever new instance is created
    def __init__(self):

        pass

    # Method called when object destroyed
    def __del__(self):

        pass






