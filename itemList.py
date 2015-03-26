class ItemList(list):
    '''
    FUNCTIONS:
        AddItem: Adds an item to the list
        
        RemoveItem: Removes an item from the list
        
        GetItem: Return a single item object from the list
        
        NumberOfItems:
    '''
    def __init__(self):
        pass
    
    def AddItem(self,Item):
        '''
        Adds an item object to the item list
        '''
        # TODO - Check the item is valid
        self.append(Item)
        
    def RemoveItem(self,Item):
        '''
        Removes an item object from the item list
        '''
        self.remove(Item)
    
    def GetItem(self,parameter):
        '''
        Searches for an item object in the itemlist given the parameter
    
        ARGS:
            parameter:
                A value to match against the item, can be
                    Int: Unique ID of the item
                    String: The title of the item
                
        RETURNS:
            Item:
                An item object matching the parameter
        '''
        # Check the type of the parameter
        if type(parameter) == int:
            parameterType = 'ID'
            
        elif type(parameter) == str:
            parameterType = 'Title'
        
        # Raise an exception if the argument is invalid
        else:
            raise TypeError('Item can only be searched on ID or title')

        # Loop over items
        for item in self:
            itemParameter = item.GetParameter(parameterType)
            # Check whether the item is the requested item
            if parameter == itemParameter:
                # Yes - Return the item matching the ID
                return item
        #If no item is found raise an exception
        # TODO - make this an ItemNotFoundException class
        raise Exception('No item found matching the ' + parameterType + ' ' + 
                        str(parameter))
        
    def NumberOfItems(self):
        return len(self)
        
class UserItemList(ItemList):
    '''
    FUNCTIONS:
        GetFines:
            Accumulates the fines from each overdue item
    '''
    def GetFines(self):
        '''
        Calculates the fines from each item in the list
            
        RETURNS:
            fine:
                Float of the total fine in pounds
        '''
        # Intitialise the fine
        fine = 0.0
        for item in self:
            fine += item.Fine()
            
        return fine
        
    def CheckoutItem(self,item):
        '''
        Adds an item to be checked out to the item list
        
        ARGS:
            item:
                The item to be checked out
        '''
        # Set the checkout on the item
        item.SetCheckout()        
        # Add the item to the list
        self.AddItem(item)
        
        return
        
    def ReturnItem(self,parameter):
        '''
        Removes an item being checked in from the UserList and resets the 
        checkout
        
        ARGS:
            parameter:
                A value to match against the item, can be
                    Int: Unique ID of the item
                    String: The title of the item
        '''
        # Find the item in this itemlist
        item = self.GetItem(parameter)
        # Reset the checkout on the item
        item.ResetCheckout()
        # Remove the item from the list
        self.RemoveItem(item)
        
        return
            





        