import datetime

class Item():
    """An Item class for use in LibrarySystem.
    """
    def __init__(self, title, ident):
        self.title = title
        self.identity = ident
        self.checkout_date = float('NaN')
        
    def set_checkout(self, date=False):
        """Given a date sets the checkout date of item.
        """
        if date == False:
            self.checkout_date = datetime.datetime.now()
        else:
            self.checkout_date = date
            
    def reset_checkout(self):
        """Resets checkout date.
        """
        
    def get_parameter(self, ptype):
        """Given a ptype string of 'ID' or 'Title' returns title or id of item.
        """
        if ptype=='ID':
            return self.identity
        elif ptype=='Title':
            return self.title
                        
    def fine(self): #, date):
        """Returns the amount of money due in fines on item.
        """
        d1 = datetime.datetime.now()
        d2 = self.checkout_date
        daysout = (d1 - d2).days #days book has been out
        fine = (daysout - self.loantime)*self.finerate #fine in pounds
        return fine
        
            
class Book(Item):
    """Subclass of Item.
    """
    finerate = 0.50 #50p/day
    loantime = 4*7 # 4weeks
        

class Journal(Item):
    """Subclass of Item.
    """
    finerate = 1.0 #50p/day
    loantime = 2*7 # 4weeks
        
        
class Dvd(Item):
    """Subclass of Item.
    """
    finerate = 2.0 #50p/day
    loantime = 1*7 # 4weeks

        
    