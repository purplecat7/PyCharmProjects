class Item():
    """An Item class for use in LibrarySystem.
    """
    def __init__(self, title, ident):
        self.title = title
        self.identity = ident
        self.checkout_date = float('NaN')
        
    def SetCheckOut(self, date):
        """Given a date sets the checkout date of item.
        """
        self.checkout_date = date
        
    def GetParameter(self, ptype):
        """Given a ptype string of 'ID' or 'Title' returns title or id of item.
        """
        if ptype=='ID':
            return self.identity
        elif ptype=='Title':
            return self.title
            
            
class Book(Item):
    """Subclass of Item.
    """
    Item.finerate = 0.50 #50p/day
    Item.loantime = 4 # 4weeks
    
    def Fine(self, date):
        """Given a date as a float (0-N), returns the amount of money due in 
        fines on item.
        """
        if date - self.checkout_date <= self.loantime:
            return 0.
        elif date - self.checkout_date > self.loantime:
            return self.finerate * (date - self.checkout_date - self.loantime)
        else:
            raise Exception('Item aint in Itemlist fool!')

        
    