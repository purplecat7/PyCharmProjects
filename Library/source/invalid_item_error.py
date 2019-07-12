class InvalidItemError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "This item does not exist"