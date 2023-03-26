from item import Item

class Book(Item):
    """ This is a subclass of Item. It has 3 class attributes set - finerate, loantime, identifier_type
    It has no methods other than those inherited from Item class """

    # Set class attributes
    loantime = 28            # Loan period in days
    finerate = 0.50          # Fine rate per week in pounts

class DVD(Item):
    """ This is a subclass of Item. It has 3 class attributes set - finerate, loantime, identifier_type
    It has no methods other than those inherited from Item class """

    # Set class attributes
    loantime = 7            # Loan period in days
    finerate = 2.0           # Fine rate per week in pounts

class Journal(Item):
    """ This is a subclass of Item. It has 3 class attributes set - finerate, loantime, identifier_type
    It has no methods other than those inherited from Item class """

    # Set class attribute
    loantime = 14               # Loan period in days
    finerate = 1.0              # Fine rate per week in pounts
