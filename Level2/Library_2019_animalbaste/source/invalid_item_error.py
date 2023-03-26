class InvalidItemError(Exception):
    def __init__(self, itemid):
        self.item = itemid

    def __str__(self):
        return "This item does not exist: " + str(self.item)
